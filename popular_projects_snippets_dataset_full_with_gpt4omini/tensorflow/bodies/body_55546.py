# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if attr_def.HasField("allowed_values"):
    allowed_list = attr_def.allowed_values.list.type
    allowed_values = ", ".join(dtypes.as_dtype(x).name for x in allowed_list)
    if dtype not in allowed_list:
        raise TypeError(
            f"Value passed to parameter '{param_name}' has DataType "
            f"{dtypes.as_dtype(dtype).name} not in list of allowed values: "
            f"{allowed_values}")
