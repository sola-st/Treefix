# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
rt1 = ragged_factory_ops.constant(
    rt_input, ragged_rank=ragged_rank, inner_shape=inner_shape)
rt2 = rebuild_ragged_tensor_with_value_rowids(rt1)
for rt in [rt1, rt2]:
    for use_placeholder in [False, True]:
        if use_placeholder:
            if default is not None:
                default = make_placeholder(default)
            rt = nest.map_structure(make_placeholder, rt, expand_composites=True)
        dt = rt.to_tensor(default_value=default, shape=shape)
        self.assertIsInstance(dt, ops.Tensor)
        self.assertEqual(rt.dtype, dt.dtype)
        if shape is not None:
            self.assertTrue(dt.shape.is_compatible_with(shape))
        else:
            self.assertTrue(dt.shape.is_compatible_with(rt.shape))
        if expected_shape is not None:
            expected = np.ndarray(expected_shape, buffer=np.array(expected))
        self.assertAllEqual(dt, expected)
