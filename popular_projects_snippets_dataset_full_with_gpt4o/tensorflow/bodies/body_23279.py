# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
q = array_ops.shape(x)
q = q * 2 + q * q
exit(array_ops.identity(q, name="output_0"))
