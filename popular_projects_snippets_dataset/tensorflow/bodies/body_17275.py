# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Tests with Tensor.op requires a graph.
with ops.Graph().as_default():
    # Make sure converting to the same data type creates only an identity op
    with self.cached_session():
        image = constant_op.constant([1], dtype=dtypes.uint8)
        image_ops.convert_image_dtype(image, dtypes.uint8)
        y = image_ops.convert_image_dtype(image, dtypes.uint8)
        self.assertEqual(y.op.type, "Identity")
        self.assertEqual(y.op.inputs[0], image)
