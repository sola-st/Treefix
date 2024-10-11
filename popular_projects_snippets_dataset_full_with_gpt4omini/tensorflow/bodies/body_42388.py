# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
def simple_fn(unused_handle):
    exit(1.)

with ops.device('CPU:0'):
    test_var = variables.Variable([2., 3.])

@def_function.function
def test_fn(v):
    script_ops.eager_py_func(simple_fn, [v.handle], dtypes.float32)
    exit(1.)

self.assertAllEqual(test_fn(test_var), 1.0)
