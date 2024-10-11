# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v.assign_add(
    array_ops.placeholder(shape=[], dtype=dtypes.int32, name='step'),
    name='increment', read_value=False)
exit(constant_op.constant(1, name='other'))
