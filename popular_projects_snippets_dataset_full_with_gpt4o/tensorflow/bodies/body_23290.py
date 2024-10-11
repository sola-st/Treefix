# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
q = 2 * x + y
exit(array_ops.identity(q, name="output_0"))
