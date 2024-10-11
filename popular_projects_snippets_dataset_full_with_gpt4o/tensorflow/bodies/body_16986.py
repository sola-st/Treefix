# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    # Shape inference works and produces expected output where possible
    rgb_shape = [7, None, 19, 3]
    gray_shape = rgb_shape[:-1] + [1]
    with self.cached_session():
        rgb_tf = array_ops.placeholder(dtypes.uint8, shape=rgb_shape)
        gray = image_ops.rgb_to_grayscale(rgb_tf)
        self.assertEqual(gray_shape, gray.get_shape().as_list())

    with self.cached_session():
        gray_tf = array_ops.placeholder(dtypes.uint8, shape=gray_shape)
        rgb = image_ops.grayscale_to_rgb(gray_tf)
        self.assertEqual(rgb_shape, rgb.get_shape().as_list())

    # Shape inference does not break for unknown shapes
    with self.cached_session():
        rgb_tf_unknown = array_ops.placeholder(dtypes.uint8)
        gray_unknown = image_ops.rgb_to_grayscale(rgb_tf_unknown)
        self.assertFalse(gray_unknown.get_shape())

    with self.cached_session():
        gray_tf_unknown = array_ops.placeholder(dtypes.uint8)
        rgb_unknown = image_ops.grayscale_to_rgb(gray_tf_unknown)
        self.assertFalse(rgb_unknown.get_shape())
