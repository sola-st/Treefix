# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires a graph.
with ops.Graph().as_default():
    image = array_ops.placeholder(dtypes.float32, shape=[55, 66, 3])
    y = image_ops.crop_to_bounding_box(image, 0, 0, 55, 66)
    self.assertTrue(y.name.startswith("crop_to_bounding_box"))
