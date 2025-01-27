# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    img = array_ops.placeholder(dtype=dtypes.float32)
    img_np = np.array((2, 2))

    with self.cached_session() as sess:
        _, _, checks = image_ops_impl._verify_compatible_image_shapes(img, img)
        with self.assertRaises(errors.InvalidArgumentError):
            sess.run(checks, {img: img_np})
