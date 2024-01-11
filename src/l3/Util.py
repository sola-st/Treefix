import os
import re
import subprocess
import libcst as cst
import json

from l3.RemoveLines import RemoveLines

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

def get_undefined_variables(src):
    undefined_variables = set()

    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = set(ast_wrapper.resolve(cst.metadata.ScopeProvider).values())
    ranges = ast_wrapper.resolve(cst.metadata.PositionProvider)
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                undefined_variables.add(node.value)
    return undefined_variables

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

def remove_lines_with_execution_error(code):
    code = remove_lines_with_syntax_error(code)
    lines_with_execution_error = True
    while lines_with_execution_error:
        with open("temp.py", "w") as f:
            f.write(code)

        try:
            subprocess.run(["python3", "temp.py"], capture_output=True, text=True, check=True)
            lines_with_execution_error = False
        except subprocess.CalledProcessError as e:
            # Extract the line number from stderr
            lines = e.stderr.splitlines()
            for line in lines:
                match = re.search(r'temp.py\", line (\d+)', line)
                if match:
                    line_with_error = int(match.group(1))
                    code = remove_lines(code, [line_with_error])
                    code = remove_lines_with_syntax_error(code)
                    with open("temp.py", "w") as f:
                        f.write(code)
                    break
    subprocess.run(["rm", "temp.py"])
    return code

def code_executes(code):
    success = True
    with open("temp.py", "w") as f:
        f.write(code)
    try:
        subprocess.run(["python3", "temp.py"], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        success = False
    subprocess.run(["rm", "temp.py"])
    return success

def install_dependencies(dependencies_dir_path, code):
    with open(f"{dependencies_dir_path}/temp.py", "w") as f:
        f.write(code)
    os.system(f"pipreqs {dependencies_dir_path} --force & pip install -r {dependencies_dir_path}/requirements.txt")
    subprocess.run(["rm", f"{dependencies_dir_path}/temp.py"])