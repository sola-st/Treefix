# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
if expected is None:
    self.fail("expected must be specified")
with self.session() as sess, self.test_scope():
    image = array_ops.placeholder(image_np.dtype)
    resized = gen_image_ops.resize_bilinear(
        image, target_shape, align_corners=align_corners)
    out = sess.run(resized, {image: image_np[np.newaxis, :, :, np.newaxis]})
    if large_tolerance:
        self.assertAllClose(
            expected[np.newaxis, :, :, np.newaxis], out, rtol=0.1, atol=0.01)
    else:
        self.assertAllClose(expected[np.newaxis, :, :, np.newaxis], out)
