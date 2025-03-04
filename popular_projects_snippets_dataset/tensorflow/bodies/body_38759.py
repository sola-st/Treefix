# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
"""Test for passing weird things into ksizes."""
with self.assertRaisesRegex(TypeError, "Expected list"):
    image = constant_op.constant([0.0])
    ksizes = math_ops.cast(
        constant_op.constant(dtype=dtypes.int16, value=[[1, 4], [5, 2]]),
        dtype=dtypes.qint16)
    strides = [1, 1, 1, 1]
    self.evaluate(
        array_ops.extract_image_patches(
            image, ksizes=ksizes, strides=strides, padding="SAME"))
