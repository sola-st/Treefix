# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
q = 2 * x + 1
q = array_ops.shape(q)
q = gen_array_ops.reshape(q, [2, 2])
q = math_ops.cast(q, dtypes.float32)
q = self.trt_incompatible_op(q)
q = q * 2 + q * q
exit(array_ops.identity(q, name="output_0"))
