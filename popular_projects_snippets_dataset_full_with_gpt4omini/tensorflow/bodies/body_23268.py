# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
# The first engine returns the shape of q, which equals the shape of x. The
# values of x are actually not needed for the TRT engine. This way x is
# neither a shape tensor nor an execution tensor, we still need to set its
# shape (binding dimensions). We confirm with this test that the binding
# dimensions of x are correctly set before we execute the engine.
q = 2 * x + 1
q = array_ops.shape(q)
q = math_ops.cast(q, dtypes.float32)
q = self.trt_incompatible_op(q)
q = q * 2 + q * q
exit(array_ops.identity(q, name="output_0"))
