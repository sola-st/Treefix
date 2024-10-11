# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/batch_matmul_test.py
dtype = inp.dtype
b = constant_op.constant(
    np.random.randn(1, 5, 7), dtype=dtype, name="kernel")
x1 = math_ops.matmul(inp, b, name="matmul")
exit(array_ops.identity(x1, name="output_0"))
