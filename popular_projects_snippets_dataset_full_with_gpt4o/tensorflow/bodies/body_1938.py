# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
if input_shape is None:
    self.fail("input_shape must be specified")
if expected is None:
    self.fail("expected must be specified")
with self.session() as sess, self.test_scope():
    dtype = dtype or np.float32
    grads = array_ops.placeholder(np.float32)
    resized = gen_image_ops.resize_bilinear_grad(
        grads,
        np.zeros([1, input_shape[0], input_shape[1], 1], dtype=dtype),
        align_corners=True)
    out = sess.run(resized, {grads: grads_np[np.newaxis, :, :, np.newaxis]})
    if large_tolerance:
        self.assertAllClose(
            expected[np.newaxis, :, :, np.newaxis], out, rtol=0.1, atol=0.01)
    else:
        self.assertAllCloseAccordingToType(
            expected[np.newaxis, :, :, np.newaxis], out)
