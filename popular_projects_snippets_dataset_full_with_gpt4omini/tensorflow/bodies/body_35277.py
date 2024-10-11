# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    for batch_shape in ([], [1], [2, 3, 4]):
        dist = make_categorical(batch_shape, 10)
        self.assertAllEqual(batch_shape, dist.batch_shape)
        self.assertAllEqual(batch_shape, dist.batch_shape_tensor())
        self.assertAllEqual([], dist.event_shape)
        self.assertAllEqual([], dist.event_shape_tensor())
        self.assertEqual(10, dist.event_size.eval())
        # event_size is available as a constant because the shape is
        # known at graph build time.
        self.assertEqual(10, tensor_util.constant_value(dist.event_size))

    for batch_shape in ([], [1], [2, 3, 4]):
        dist = make_categorical(
            batch_shape, constant_op.constant(
                10, dtype=dtypes.int32))
        self.assertAllEqual(len(batch_shape), dist.batch_shape.ndims)
        self.assertAllEqual(batch_shape, dist.batch_shape_tensor())
        self.assertAllEqual([], dist.event_shape)
        self.assertAllEqual([], dist.event_shape_tensor())
        self.assertEqual(10, dist.event_size.eval())
