# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt1 = ragged_factory_ops.constant(rt, ragged_rank=rt_ragged_rank)
rt1._set_shape(shape)
rt1.shape.assert_is_compatible_with(shape)
if shape is not None:
    self.assertIsNot(rt1.shape.rank, None)
    for a, b in zip(rt1.shape, shape):
        if b is not None:
            self.assertEqual(a, b)
