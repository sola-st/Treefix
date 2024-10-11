# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
q = array_ops.shape(x)
z = y * y + y
z = gen_array_ops.reshape(z, q)
out_0 = array_ops.identity(q, name="output_0")
out_1 = array_ops.identity(z, name="output_1")
exit((out_0, out_1))
