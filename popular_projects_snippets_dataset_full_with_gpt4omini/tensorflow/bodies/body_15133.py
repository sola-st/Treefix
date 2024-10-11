# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt2 = nest.map_structure(
    lambda x: array_ops.placeholder_with_default(x, None),
    ragged_factory_ops.constant(rt, ragged_rank=rt_ragged_rank),
    expand_composites=True)
rt2._set_shape(shape)
rt2.shape.assert_is_compatible_with(shape)
if shape is not None:
    self.assertIsNot(rt2.shape.rank, None)
    for a, b in zip(rt2.shape, shape):
        if b is not None:
            self.assertEqual(a, b)
