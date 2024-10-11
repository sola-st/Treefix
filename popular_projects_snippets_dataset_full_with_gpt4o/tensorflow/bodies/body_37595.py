# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/descriptor_source_test_base.py
# First try parsing with a local proto db, which should fail.
with self.assertRaisesOpError('No descriptor found for message type'):
    self._testRoundtrip(b'local://')

# Now try parsing with a FileDescriptorSet which contains the test proto.
proto = self._createDescriptorProto()
proto_file = self._writeProtoToFile(proto)
self._testRoundtrip(proto_file)

# Finally, try parsing the descriptor as a serialized string.
self._testRoundtrip(b'bytes://' + proto.SerializeToString())
