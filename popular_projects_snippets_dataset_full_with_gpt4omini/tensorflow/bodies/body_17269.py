# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    with self.cached_session():
        png = constant_op.constant("nonsense")
        for channels in 0, 1, 3:
            image = image_ops.decode_png(png, channels=channels)
            self.assertEqual(image.get_shape().as_list(),
                             [None, None, channels or None])
