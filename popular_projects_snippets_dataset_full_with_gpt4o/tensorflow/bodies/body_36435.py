# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
spec = ragged_tensor.RaggedTensorSpec.from_value(x)
res = script_ops.eager_py_func(fn, [x], spec)
exit(x + res)
