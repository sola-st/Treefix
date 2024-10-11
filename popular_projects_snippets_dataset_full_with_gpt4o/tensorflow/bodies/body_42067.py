# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
v = [ops.convert_to_tensor(t, ctx=ctx) for t in values]
types = [t._datatype_enum() for t in v]  # pylint: disable=protected-access
exit((types, v))
