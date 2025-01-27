# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/descriptor_source_test_base.py
# Numpy silently truncates the strings if you don't specify dtype=object.
in_bufs = np.array(
    [test_base.ProtoOpTestBase.simple_test_case().SerializeToString()],
    dtype=object)
message_type = 'tensorflow.contrib.proto.TestCase'
field_names = ['values', 'shapes', 'sizes', 'fields']
tensor_types = [dtypes.string, dtypes.int32, dtypes.int32, dtypes.string]

with self.cached_session() as sess:
    sizes, field_tensors = self._decode_module.decode_proto(
        in_bufs,
        message_type=message_type,
        field_names=field_names,
        output_types=tensor_types,
        descriptor_source=descriptor_source)

    out_tensors = self._encode_module.encode_proto(
        sizes,
        field_tensors,
        message_type=message_type,
        field_names=field_names,
        descriptor_source=descriptor_source)

    out_bufs, = sess.run([out_tensors])

    # Check that the re-encoded tensor has the same shape.
    self.assertEqual(in_bufs.shape, out_bufs.shape)

    # Compare the input and output.
    for in_buf, out_buf in zip(in_bufs.flat, out_bufs.flat):
        # Check that the input and output serialized messages are identical.
        # If we fail here, there is a difference in the serialized
        # representation but the new serialization still parses. This could
        # be harmless (a change in map ordering?) or it could be bad (e.g.
        # loss of packing in the encoding).
        self.assertEqual(in_buf, out_buf)
