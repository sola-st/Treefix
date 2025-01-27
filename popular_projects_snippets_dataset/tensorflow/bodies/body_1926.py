# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
if expected is None:
    self.fail("expected must be specified")
with self.session() as sess, self.test_scope():
    image = array_ops.placeholder(image_np.dtype)
    resized = gen_image_ops.resize_nearest_neighbor(
        image,
        target_shape,
        align_corners=align_corners,
        half_pixel_centers=half_pixel_centers)
    out = sess.run(resized, {image: image_np[np.newaxis, :, :, np.newaxis]})
    if large_tolerance:
        self.assertAllClose(
            expected[np.newaxis, :, :, np.newaxis], out, rtol=2e-4, atol=2e-4)
    else:
        self.assertAllClose(expected[np.newaxis, :, :, np.newaxis], out)
