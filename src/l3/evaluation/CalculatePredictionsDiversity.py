import argparse
import atexit
import json
import os
import subprocess
import libcst as cst
import pandas as pd
import fcntl

from tempfile import NamedTemporaryFile
from ..Util import gather_files


parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="CSV files containing the predictions from the model", nargs="+")

def get_variable_names(code): 
    var_names = set()

    try:
        # Parse the source code
        ast = cst.parse_module(code)

        # Define a visitor to traverse the AST
        class VariableVisitor(cst.CSTVisitor):
            def visit_Import(self, node):
                for import_alias in node.names:
                    if import_alias.asname:
                        import_name = import_alias.asname.name.value
                    elif isinstance(import_alias.name, cst.Attribute):
                        import_name = f"{import_alias.name.value.value}.{import_alias.name.attr.value}"
                    else:
                        import_name = import_alias.name.value
                    if isinstance(import_name, str):
                        var_names.add(import_name)
                return node

            def visit_Assign(self, node):
                if isinstance(node.targets[0].target, cst.Name):
                    var_name = node.targets[0].target.value
                    if isinstance(var_name, str):
                        var_names.add(var_name)
                elif isinstance(node.targets[0].target, cst.Attribute) or isinstance(node.targets[0].target, cst.Subscript):
                    # Do not count attribute assignments nor subscripts
                    pass
                else:
                    # Tuple unpacking
                    for element in node.targets[0].target.elements:
                        var_name = element.value.value
                        if isinstance(var_name, str):
                            var_names.add(var_name)
                return node

            def visit_FunctionDef(self, node):
                # Ignore function definitions
                pass

            def visit_ClassDef(self, node):
                # Ignore class definitions
                pass

        # Visit each node in the AST
        ast_wrapper = cst.metadata.MetadataWrapper(ast)
        variable_visitor = VariableVisitor()
        ast_wrapper.visit(variable_visitor)
    except:
        pass

    return var_names

def serialize_value(value):
    if type(value).__name__ == "module":
        return str(value)
    try:
        # Distinguish primitive and non-primitive objects
        attributes = value.__dict__
        # Attributes and methods
        properties = dir(value)
        return properties
    except:
        return str(value)
    
def is_valid_json(dictionary):
    try:
        aux = json.loads(json.dumps(dictionary))
        return True
    except:
        return False

def get_types_and_values(*args):
    file_name = 'treefix_types_and_values.json'
    if os.path.isfile(file_name):
        with open(file_name, "r") as f:
            types_and_values = json.load(f)
    else:
        types_and_values = {}

    for arg in args:
        arg_type = type(arg).__name__
        serialized_value = serialize_value(arg)
        
        if arg_type not in types_and_values:
            types_and_values[arg_type] = [serialized_value]
        elif serialized_value not in types_and_values[arg_type]:
            types_and_values[arg_type].append(serialized_value)

    # Only save valid json values
    if is_valid_json(types_and_values):
        with open(file_name, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            json.dump(types_and_values, f)
            fcntl.flock(f, fcntl.LOCK_UN)
    

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    for file in files:
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            print(f"row {index}")
            predictions = json.loads(row['predictions'])

            prediction_id = 0
            for prediction in predictions:
                print(f"Analyzing file: {file}")
                print("=====================================================")
                print(f"Prediction id: {prediction_id}")
                imports_code = '\n'.join(prediction['imports'])
                prediction_code = '\n'.join(prediction['initialization'])

                variable_names = get_variable_names(f"{imports_code}\n\n{prediction_code}")

                cleaned_variable_names = ""  
                for var_name in variable_names:
                    if cleaned_variable_names:
                        cleaned_variable_names = cleaned_variable_names + f", {var_name}" 
                    else:
                        cleaned_variable_names = var_name

                if cleaned_variable_names:
                    code = "from l3.evaluation.CalculatePredictionsDiversity import get_types_and_values\n\n"
                    code = code + f"{imports_code}\n\n{prediction_code}\n\nget_types_and_values({cleaned_variable_names})"

                    with NamedTemporaryFile("w", delete=False) as tmp_file:
                        tmp_file.write(code)
                        atexit.register(os.unlink, tmp_file.name) 

                    try:
                        process = subprocess.run(["python3", tmp_file.name], stdout=subprocess.PIPE)
                        print(process.stdout.decode('UTF-8'))
                    except subprocess.CalledProcessError as e:
                        print(e.stderr)

                prediction_id += 1