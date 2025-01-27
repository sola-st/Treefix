# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# I pulled this out of the tensorflow test case, so that I could have
# more control.
# However this error is being generated, it confuses assertRaises,
# but it exists.
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            r'Cannot broadcast'):
    sess = session.Session()
    with sess.as_default():
        origin = _to_ragged_tensor_from_lengths(origin_values, origin_lengths)
        expected_shape = DynamicRaggedShape.from_lengths(expected_lengths)

        rt = dynamic_ragged_shape.broadcast_to(origin, expected_shape)
        sess.run([rt])
