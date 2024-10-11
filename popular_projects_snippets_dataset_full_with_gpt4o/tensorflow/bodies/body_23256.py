# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
outputs = []
# Here we test two types of reshapes, one changes the batch dimension and
# the other does not. Note that we're not able to test reshaping to
# scalar, since TRT requires input tensor to be of rank at least 2, so a
# reshape with scalar input will be filtered out of the segment before
# conversion.
#
# These reshapes happen at batch dimension, thus conversion should fail.
orig_shape = constant_op.constant([-1, 24, 24, 2], name="original_shape")
for shape in [[2, 50, 24, 24, 2], [-1, 50, 24, 24, 2], [2, 50, -1, 24, 2]]:
    incompatible_reshape = array_ops.reshape(inp, shape)
    reshape_back = array_ops.reshape(incompatible_reshape, orig_shape)
    outputs.append(self.trt_incompatible_op(reshape_back))
# Add another block with many reshapes that don't change the batch
# dimension.
compatible_reshape = array_ops.reshape(
    inp, [-1, 24 * 24, 2], name="reshape-0")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [100, 24, -1], name="reshape-1")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [100, 24 * 2, 24], name="reshape-2")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [-1, 24, 24 * 2], name="reshape-3")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [-1, 6, 4, 24, 2], name="reshape-4")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [-1, 6, 4, 6, 4, 2, 1], name="reshape-5")
compatible_reshape = array_ops.reshape(
    compatible_reshape, [-1, 24, 24, 2], name="reshape-6")
outputs.append(self.trt_incompatible_op(compatible_reshape))
exit(math_ops.add_n(outputs, name="output_0"))
