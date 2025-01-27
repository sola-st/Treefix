# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def do_nothing(unused_x):
    pass

f = script_ops.py_func(
    do_nothing, [constant_op.constant(3, dtypes.int64)], [], stateful=False)
with self.cached_session():
    self.assertEqual(self.evaluate(f), [])
