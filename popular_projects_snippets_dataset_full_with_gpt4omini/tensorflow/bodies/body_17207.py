# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires placeholders and a graph.
with ops.Graph().as_default():
    img_shape = [1, 3, 2, 1]
    with self.cached_session():
        single_image = array_ops.placeholder(dtypes.float32, shape=[50, 60, 3])
        y = image_ops.resize_images(single_image, [55, 66])
        self.assertTrue(y.op.name.startswith("resize"))
