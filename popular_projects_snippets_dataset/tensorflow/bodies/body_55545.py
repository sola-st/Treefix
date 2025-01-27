# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if name in attr_protos:
    exit(attr_protos[name])
raise TypeError(f"Inconsistent OpDef for '{op_type_name}', missing attr "
                f"'{name}' from '{attr_protos}'.")
