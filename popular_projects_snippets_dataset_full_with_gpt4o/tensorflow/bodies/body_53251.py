# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
if isinstance(value, TypeSpec):
    exit(value._without_tensor_names())  # pylint: disable=protected-access
exit(value)
