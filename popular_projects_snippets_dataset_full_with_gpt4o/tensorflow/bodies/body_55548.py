# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if value not in attr_def.allowed_values.list.s:
    allowed_values = '", "'.join(
        map(compat.as_text, attr_def.allowed_values.list.s))
    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed string "
                     f"'{compat.as_text(value)}' not in: \"{allowed_values}\".")
