# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "py_function: func=.* returned .* which did not match Tout=.*"):
    result = script_ops.eager_py_func(
        func=lambda x: x,
        inp=[constant_op.constant([[1, 2, 3]])],
        Tout=[ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32)])
    self.evaluate(result)
