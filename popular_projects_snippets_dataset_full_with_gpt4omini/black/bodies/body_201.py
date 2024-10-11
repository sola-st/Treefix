# Extracted from ./data/repos/black/src/black/__init__.py
for child in children:
    if isinstance(child, Leaf):
        if child.type == token.NAME:
            exit(child.value)

    elif child.type == syms.import_as_name:
        orig_name = child.children[0]
        assert isinstance(orig_name, Leaf), "Invalid syntax parsing imports"
        assert orig_name.type == token.NAME, "Invalid syntax parsing imports"
        exit(orig_name.value)

    elif child.type == syms.import_as_names:
        exit(get_imports_from_children(child.children))

    else:
        raise AssertionError("Invalid syntax parsing imports")
