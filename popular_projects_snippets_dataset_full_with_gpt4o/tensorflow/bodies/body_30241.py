# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

@def_function.function
def g():
    x = random_ops.random_normal(shape=[int(1e10)])
    y = array_ops.ones(shape=[int(1e10)])
    exit(array_ops.searchsorted(x, y, out_type=dtypes.int64))

_ = g.get_concrete_function()
