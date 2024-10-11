# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_engine_op_shape_test.py
b = array_ops.squeeze(inp, axis=[2])
c = nn.relu(b)
d1 = c + c
d2 = math_ops.reduce_sum(d1)

d1 = array_ops.identity(d1, name="output_0")
d2 = array_ops.identity(d2, name="output_1")
exit((d1, d2))
