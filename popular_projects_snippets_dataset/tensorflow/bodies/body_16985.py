# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# tests whether the grayscale_to_rgb function raises
# an exception if the input images' last dimension is
# not of size 1, i.e. the images have shape
# [batch size, height, width] or [height, width]

# tests if an exception is raised if a three dimensional
# input is used, i.e. the images have shape [batch size, height, width]
with self.cached_session():
    # 3-D input with batch dimension.
    x_np = np.array([[1, 2]], dtype=np.uint8).reshape([1, 1, 2])

    x_tf = constant_op.constant(x_np, shape=x_np.shape)

    # this is the error message we expect the function to raise
    err_msg = "Last dimension of a grayscale image should be size 1"
    with self.assertRaisesRegex(ValueError, err_msg):
        image_ops.grayscale_to_rgb(x_tf)

    # tests if an exception is raised if a two dimensional
    # input is used, i.e. the images have shape [height, width]
with self.cached_session():
    # 1-D input without batch dimension.
    x_np = np.array([[1, 2]], dtype=np.uint8).reshape([2])

    x_tf = constant_op.constant(x_np, shape=x_np.shape)

    # this is the error message we expect the function to raise
    err_msg = "must be at least two-dimensional"
    with self.assertRaisesRegex(ValueError, err_msg):
        image_ops.grayscale_to_rgb(x_tf)
