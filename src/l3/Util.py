import os
import re
import json
import subprocess
import libcst as cst

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
        self.undefined_variables = set()
        self.undefined_variables_locations = undefined_variables_locations
        self.ranges = ranges

    def visit_Attribute(self, node):
        for undefined_variable_location in self.undefined_variables_locations:
            variable, location = undefined_variable_location
            if isinstance(node.value, cst.Name) and node.value.value == variable:
                self.undefined_variables.add(f'{node.value.value}.{node.attr.value}')
                break
        return node

def get_undefined_variables(src):
    undefined_variables = set()
    
    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = set(ast_wrapper.resolve(cst.metadata.ScopeProvider).values())
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                undefined_variables.add(node.value)

    return undefined_variables

def get_undefined_attributes_methods(src):
    undefined_variables_locations = set()

    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = set(ast_wrapper.resolve(cst.metadata.ScopeProvider).values())
    ranges = ast_wrapper.resolve(cst.metadata.PositionProvider)
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                location = ranges[node].start
                undefined_variables_locations.add((node.value, location))

    undefined_finder = UndefinedFinder(undefined_variables_locations, ranges)
    ast_wrapper.visit(undefined_finder)

    return undefined_finder.undefined_variables

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

def remove_lines_with_execution_error(code):
    code = remove_lines_with_exit(code)
    code = remove_lines_with_syntax_error(code)
    lines_with_execution_error = True
    while lines_with_execution_error:
        with open("temp_.py", "w") as f:
            f.write(code)

        try:
            subprocess.run(["python3", "temp_.py"], capture_output=True, text=True, check=True, timeout=30)
            lines_with_execution_error = False
        except subprocess.CalledProcessError as e:
            print(e)
            # Extract the line number from stderr
            lines = e.stderr.splitlines()
            for line in lines:
                match = re.search(r'temp_.py\", line (\d+)', line)
                if match:
                    line_with_error = int(match.group(1))
                    print(line_with_error)
                    code = remove_lines(code, [line_with_error])
                    code = remove_lines_with_syntax_error(code)
                    with open("temp_.py", "w") as f:
                        f.write(code)
                    break
        except subprocess.TimeoutExpired:
            code = ""
            break

    subprocess.run(["rm", "temp_.py"])
    return code

def code_executes(code):
    success = False
    with open("temp.py", "w") as f:
        f.write(code)
    try:
        subprocess.run(["python3", "temp.py"], capture_output=True, text=True, check=True, timeout=30)
        success = True
    except:
        pass
    subprocess.run(["rm", "temp.py"])
    return success

def install_dependencies(dependencies_dir_path, code):
    with open(f"{dependencies_dir_path}/temp.py", "w") as f:
        f.write(code)
    os.system(f"pipreqs {dependencies_dir_path} --force")

    with open(f"{dependencies_dir_path}/requirements.txt", "r") as fp:
        lines = fp.readlines()

    with open(f"{dependencies_dir_path}/requirements.txt", "w") as fp:
        for line in lines:
            if "l3.egg==info" not in line:
                fp.write(line)

    os.system(f"pip install -r {dependencies_dir_path}/requirements.txt")
    subprocess.run(["rm", f"{dependencies_dir_path}/temp.py"])

def count_lines(file_path):
    total_lines = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("_l_("):
                total_lines += 1
    return total_lines
