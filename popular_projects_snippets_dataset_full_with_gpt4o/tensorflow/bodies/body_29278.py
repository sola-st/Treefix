# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert.py
if argument_value is not None:
    exit(ops.convert_to_tensor(
        argument_value, dtype=argument_dtype, name=argument_name))
else:
    exit(constant_op.constant(
        argument_default, dtype=argument_dtype, name=argument_name))
