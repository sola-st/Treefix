import re
import json
import argparse
import libcst as cst
from .Util import gather_files

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files to instrument or .txt file with all file paths", nargs="+")

def analyze_file(file_path):
    with open(file_path, "r") as file:
        src = file.read()

    undefined_elements = set()

    ast = cst.parse_module(src)
    ast_wrapper = cst.metadata.MetadataWrapper(ast)
    scopes = set(ast_wrapper.resolve(cst.metadata.ScopeProvider).values())
    ranges = ast_wrapper.resolve(cst.metadata.PositionProvider)
    for scope in scopes:
        for access in scope.accesses:
            if len(access.referents) == 0:
                node = access.node
                undefined_elements.add(node.value)
                # location = ranges[node].start
                # print(
                #     f"Warning on line {location.line:2d}, column {location.column:2d}: Name reference `{node.value}` is not defined."
                # )

    undefined_elements_file_path = re.sub(r"\.py$", ".json", file_path)
    data = {
        'undefined_elements': list(undefined_elements)
    }

    json_object = json.dumps(data, indent=4)
    with open(undefined_elements_file_path, "w") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    args = parser.parse_args()
    files = gather_files(args.files)
    for file_path in files:
        print(f"Analyzing {file_path}")
        analyze_file(file_path)