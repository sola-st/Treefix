# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if attr_def.has_minimum and length < attr_def.minimum:
    raise ValueError(f"Attr '{param_name}' of '{op_type_name}' Op passed list "
                     f"of length {length} less than minimum "
                     f"{attr_def.minimum}.")
