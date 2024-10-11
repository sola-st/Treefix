# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py

field_names = [f.name for f in fields]
out_types = [f.dtype for f in fields]

with self.cached_session() as sess:
    sizes, field_tensors = self._decode_module.decode_proto(
        in_bufs,
        message_type=message_type,
        field_names=field_names,
        output_types=out_types)

    out_tensors = self._encode_module.encode_proto(
        sizes,
        field_tensors,
        message_type=message_type,
        field_names=field_names)

    out_bufs, = sess.run([out_tensors])

    # Check that the re-encoded tensor has the same shape.
    self.assertEqual(in_bufs.shape, out_bufs.shape)

    # Compare the input and output.
    for in_buf, out_buf in zip(in_bufs.flat, out_bufs.flat):
        in_obj = test_example_pb2.TestValue()
        in_obj.ParseFromString(in_buf)

        out_obj = test_example_pb2.TestValue()
        out_obj.ParseFromString(out_buf)

        # Check that the deserialized objects are identical.
        self.assertEqual(in_obj, out_obj)

        # Check that the input and output serialized messages are identical.
        # If we fail here, there is a difference in the serialized
        # representation but the new serialization still parses. This could
        # be harmless (a change in map ordering?) or it could be bad (e.g.
        # loss of packing in the encoding).
        self.assertEqual(in_buf, out_buf)
