# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
if context.executing_eagerly():
    expected_error = (errors.InvalidArgumentError,
                      r'Invalid shape for field double_value.')
else:
    expected_error = (ValueError,
                      r'Shape must be at least rank 2 but is rank 0')
with self.assertRaisesRegexp(*expected_error):
    self.evaluate(
        self._encode_module.encode_proto(
            sizes=1,
            values=[np.double(1.0)],
            message_type='tensorflow.contrib.proto.TestValue',
            field_names=['double_value']))
