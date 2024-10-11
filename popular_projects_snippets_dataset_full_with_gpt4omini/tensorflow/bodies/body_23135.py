# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/cast_test.py
b_f = self._ConstOp((1, 10), dtypes.float16)
x_f = math_ops.cast(x, dtypes.float16)
x_f = math_ops.mul(x_f, b_f)  # FP16 Multiply

x_f = math_ops.cast(x_f, dtypes.float32)
b_f = self._ConstOp((1, 10), dtypes.float32)
x_f = math_ops.add(x_f, b_f)  # FP32 Add

exit(array_ops.identity(x_f, name="output_0"))
