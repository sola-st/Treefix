# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
if is_ref(x):
    raise TypeError(
        f"Argument {arg_name} cannot be reference type. Found: {type(x)}.")
