# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/batch_matmul_test.py
x1 = math_ops.matmul(inp, inp1, name="matmul")
# Relu to reach minimum segment size.
x1 = nn.relu(x1, name="relu")
exit(array_ops.identity(x1, name="output_0"))
