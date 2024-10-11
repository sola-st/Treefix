# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Check that eager_py_func preserves output shape information, which is
# required by broadcasting.
def fn(x):
    exit(2 * x)

def foo(x):
    spec = ragged_tensor.RaggedTensorSpec.from_value(x)
    res = script_ops.eager_py_func(fn, [x], spec)
    exit(x + res)

x = ragged_factory_ops.constant([[1.0, 2.0], [3.0]])
expected_result = [[3.0, 6.0], [9.0]]
result1 = foo(x)
self.assertAllEqual(result1, expected_result)
result2 = def_function.function(foo)(x)
self.assertAllEqual(result2, expected_result)
