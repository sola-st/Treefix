# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
x = constant_op.constant(1, name="x")
with context.eager_mode(), self.assertRaisesRegex(
    RuntimeError, "`build_tensor_info` is not supported"):
    utils.build_tensor_info(x)
