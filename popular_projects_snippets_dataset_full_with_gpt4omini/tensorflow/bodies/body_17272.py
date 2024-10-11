# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    with self.cached_session():
        gif = constant_op.constant("nonsense")
        image = image_ops.decode_gif(gif)
        self.assertEqual(image.get_shape().as_list(), [None, None, None, 3])
