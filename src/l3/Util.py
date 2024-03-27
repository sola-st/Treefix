import atexit
import os
from os.path import join
import re
import json
import subprocess
import libcst as cst
from time import perf_counter
from tempfile import NamedTemporaryFile, TemporaryDirectory
import fcntl
from typing import Optional, Tuple

from .RemoveLines import RemoveLines
from .IIDS import IIDs
from .Hyperparams import Hyperparams as param


def gather_files(files_arg, suffix=".py"):
    if all([f.endswith(".txt") for f in files_arg]):
        files = []
        for f in files_arg:
            with open(f) as fp:
                for line in fp.readlines():
                    files.append(line.rstrip())
    else:
        for f in files_arg:
            if not f.endswith(suffix):
                raise Exception(f"Incorrect argument, expected {suffix} file: {f}")
        files = files_arg
    return files

class UndefinedFinder(cst.CSTVisitor):
    def __init__(self, undefined_variables_locations, ranges):
        super().__init__()
        self.undefined_variables = []
        self.undefined_variables_locations = undefined_variables_locations
        self.ranges = ranges

    def visit_Attribute(self, node):
        for undefined_variable_location in self.undefined_variables_locations:
            variable, location = undefined_variable_location
            if isinstance(node.value, cst.Name) and node.value.value == variable:
                self.undefined_variables.append(f'{node.value.value}.{node.attr.value}')
                break
        return node

def get_undefined_variables(src):
    undefined_variables = []  # using a list here to get a deterministic order
    
    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = ast_wrapper.resolve(cst.metadata.ScopeProvider).values()
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                undefined_variables.append(node.value)

    # remove duplicates
    undefined_variables = list(dict.fromkeys(undefined_variables))

    return undefined_variables

def get_undefined_attributes_methods(src):
    undefined_variables_locations = []  # using a list here to get a deterministic order

    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = ast_wrapper.resolve(cst.metadata.ScopeProvider).values()
    ranges = ast_wrapper.resolve(cst.metadata.PositionProvider)
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                location = ranges[node].start
                undefined_variables_locations.append((node.value, location))

    undefined_finder = UndefinedFinder(undefined_variables_locations, ranges)
    ast_wrapper.visit(undefined_finder)

    undefined_attributes = undefined_finder.undefined_variables
    # remove duplicates
    undefined_attributes = list(dict.fromkeys(undefined_attributes))

    return undefined_attributes

def add_comment_to_uncovered_lines(instrumented_code, covered_lines):
    updated_code = []
    code = instrumented_code.split('\n')
    updated_code = []

    triple_quotes = 0

    for line_index in range(len(code)-1):
        if code[line_index].strip() != '' and code[line_index] != '# L3: DO NOT INSTRUMENT':
            if not code[line_index].strip().startswith('"""') and code[line_index].strip()[0] != '#' and not triple_quotes % 2:
                if "_l_" not in code[line_index]:
                    covered_line = False
                    for iid in covered_lines:
                        if f"_l_({iid})" in code[line_index+1]:
                            updated_code.append(code[line_index])
                            covered_line = True
                            break
                    if not covered_line:
                        updated_code.append(f"{code[line_index]} # uncovered")
            else:
                updated_code.append(code[line_index])
                if code[line_index].strip().startswith('"""'):
                    triple_quotes += 1
                if len(code[line_index].strip()) > 3 and code[line_index].strip().endswith('"""'):
                    triple_quotes += 1
        
    if "_l_" not in code[-1]:
        updated_code.append(code[-1]) 

    return '\n'.join(updated_code[1:])
    
def get_json_info(raw_json):
    try:
        info = json.loads(raw_json)
    except json.JSONDecodeError:
        try:
            info = json.loads(raw_json.replace("'", '"').replace('= "', "= '").replace('""', '\'"'))
        except:
            info = {
                'imports': [],
                'initialization': []
            }
    return info

def remove_lines(code, lines_to_remove):
    ast = cst.parse_module(code)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    code_modifier = RemoveLines(lines_to_remove)
    new_ast = ast_wrapper.visit(code_modifier)
    return new_ast.code.strip()

def remove_lines_with_undefined_variables(code):
    lines_to_remove = []
    ast = cst.parse_module(code)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = set(ast_wrapper.resolve(cst.metadata.ScopeProvider).values())
    ranges = ast_wrapper.resolve(cst.metadata.PositionProvider)
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                location = ranges[node].start
                lines_to_remove.append(location.line)
    return remove_lines(code, lines_to_remove)

def remove_lines_with_syntax_error(code):
    lines_with_syntax_error = True
    while lines_with_syntax_error:
        try:
            ast = cst.parse_module(code)
            lines_with_syntax_error = False
        except cst.ParserSyntaxError as e:
            line = e.raw_line - 1
            temp = code.split('\n')
            temp.pop(line)
            code = '\n'.join(temp)
    return code

def remove_lines_with_exit(code):
    updated_code = []
    code = code.split('\n')
    for line in code:
        if 'exit(' not in line:
            updated_code.append(line)
    return '\n'.join(updated_code)

def remove_lines_with_package(code, package):
    updated_code = []
    code = code.split('\n')
    for line in code:
        if package not in line:
            updated_code.append(line)
    return '\n'.join(updated_code)

def remove_lines_with_execution_error(code):
    code = remove_lines_with_exit(code)
    code = remove_lines_with_syntax_error(code)
    while True:
        result = execute_and_capture_error(code)
        print(result)
        if result is None:
            break # code runs without errors

        exception, line_number, error_msg = result
        if isinstance(exception, subprocess.TimeoutExpired):
            code = ""
            break # code times out
        elif line_number == "" and "python package requires root access" in error_msg:
            package = error_msg.split(":")[0]
            code = remove_lines_with_package(code, package)
        else:
            code = remove_lines(code, [line_number])
        code = remove_lines_with_syntax_error(code)    
    
    return code

def execute_and_capture_error(code) -> Optional[Tuple[BaseException, int, str]]:
    """
    Tries to execute the given code and returns either
     * None if the code executes successfully, or
     * (exception, line_number, message) if Python raises an exception
    """
    with NamedTemporaryFile("w", delete=False) as tmp_file:
        tmp_file.write(code)
        atexit.register(os.unlink, tmp_file.name) 
    try:
        subprocess.run(["python3", tmp_file.name], capture_output=True, text=True, check=True, timeout=30)
    except subprocess.CalledProcessError as e:
        print(e)
        # Extract the line number from stderr
        lines = e.stderr.splitlines()
        print(lines)
        line_number = ""
        for line in lines:
            match = re.search(rf'{tmp_file.name}\", line (\d+)', line)
            if match:
                line_number = int(match.group(1))
        error_msg = '\n'.join(lines[-2:])
        return e, line_number, error_msg
    except subprocess.TimeoutExpired as e:
        return e, -1, "Timeout"
    return None

install_dependencies_counter = 0
dependencies = []

def install_dependencies(dependencies_dir_path, code):
    global install_dependencies_counter
    start = perf_counter()  
    global dependencies

    # check for dependencies of the code using "pipreqs"
    with TemporaryDirectory() as tmp_dir:
        with open(join(tmp_dir, "temp.py"), "w") as f:
            f.write(code)
        pipreqs_result = subprocess.run(["pipreqs", tmp_dir, "--force"], capture_output=True, text=True)
        if pipreqs_result.returncode != 0:
            print(f"pipreqs failed:\n{pipreqs_result.stderr}")
            return

        with open(join(tmp_dir, "requirements.txt"), "r") as f:
            lines = f.readlines()

    # check if any of the dependencies are new
    additional_dependencies = []
    for line in lines:
        if line != "\n" and "l3.egg==info" not in line and line not in dependencies:
            additional_dependencies.append(line)
            dependencies.append(line)
    
    # add any new dependencies to the requirements.txt file and run "pip install"
    if additional_dependencies:
        with open(join(dependencies_dir_path, "requirements.txt"), "w") as fp:
            fcntl.flock(fp, fcntl.LOCK_EX)
            fp.write(''.join(additional_dependencies))
            fcntl.flock(fp, fcntl.LOCK_UN)
        os.system(f"pip install -r {dependencies_dir_path}/requirements.txt")

    install_dependencies_counter += (perf_counter() - start)
    print(f"Total spent in install_dependencies(): {install_dependencies_counter} secs")
    print(f"Content of requirements.txt:\n{lines}(end)")

def count_lines(file_path):
    total_lines = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("_l_("):
                total_lines += 1
    return total_lines