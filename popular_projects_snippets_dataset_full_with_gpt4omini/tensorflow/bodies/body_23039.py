# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
q = math_ops.abs(x1)
q = q + 1.0
q = q * 3.0
q = array_ops.squeeze(q, 0)
q = math_ops.abs(q)
q = q + 5.0
exit(array_ops.identity(q, name="output_0"))
