# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
if element_op is None:
    exit(None)

def list_op(values):
    [value] = values
    exit(element_op(value))

exit(list_op)
