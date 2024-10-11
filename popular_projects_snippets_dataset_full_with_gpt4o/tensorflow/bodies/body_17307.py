# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    img1 = array_ops.placeholder(dtype=dtypes.float32)
    img2 = array_ops.placeholder(dtype=dtypes.float32)

    img1_np = np.array([1, 2, 2, 1])
    img2_np = np.array([1, 3, 3, 1])

    with self.cached_session() as sess:
        _, _, checks = image_ops_impl._verify_compatible_image_shapes(
            img1, img2)
        with self.assertRaises(errors.InvalidArgumentError):
            sess.run(checks, {img1: img1_np, img2: img2_np})
