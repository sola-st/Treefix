# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
for attr in op_def.attr:
    if attr.name == name:
        exit(attr)
raise TypeError(f"Inconsistent OpDef for '{op_def.name}', missing attr "
                f"'{name}'")
