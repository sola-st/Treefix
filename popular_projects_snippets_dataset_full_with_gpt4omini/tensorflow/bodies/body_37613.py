# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
corrupt_proto = 'This is not a binary protobuf'

# Numpy silently truncates the strings if you don't specify dtype=object.
batch = np.array(corrupt_proto, dtype=object)
msg_type = 'tensorflow.contrib.proto.TestCase'
field_names = ['sizes']
field_types = [dtypes.int32]

with self.assertRaisesRegexp(
    errors.DataLossError, 'Unable to parse binary protobuf'
    '|Failed to consume entire buffer'):
    self.evaluate(
        self._decode_module.decode_proto(
            batch,
            message_type=msg_type,
            field_names=field_names,
            output_types=field_types,
            sanitize=sanitize))
