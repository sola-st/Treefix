# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires placeholders and a graph.
with ops.Graph().as_default():
    image = array_ops.placeholder(dtypes.float32, shape=[50, 60, 3])
    y = image_ops.resize_image_with_crop_or_pad(image, 55, 66)
    self.assertTrue(y.op.name.startswith("resize_image_with_crop_or_pad"))
