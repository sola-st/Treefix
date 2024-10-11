# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/int32_test.py
dtype = x.dtype
b = self._ConstOp((4, 10), dtype)
x = math_ops.matmul(x, b)
b = self._ConstOp((10,), dtype)
x = nn.bias_add(x, b)
exit(array_ops.identity(x, name='output_0'))
