# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def fn(a):
    exit(str(a.dtype))

x = constant_op.constant("x", dtype=dtypes.string)
output = script_ops.eager_py_func(fn, inp=[x], Tout=dtypes.string)
self.assertEqual(self.evaluate(output), "<dtype: 'string'>".encode("utf8"))
