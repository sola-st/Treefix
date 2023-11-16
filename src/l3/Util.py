import libcst as cst

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

def get_undefined_elements(file_path):
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
    
    return undefined_elements