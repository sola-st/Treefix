# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
# Invalid field name
with self.assertRaisesOpError('Unknown field: non_existent_field'):
    self.evaluate(
        self._encode_module.encode_proto(
            sizes=[[1]],
            values=[np.array([[0.0]], dtype=np.int32)],
            message_type='tensorflow.contrib.proto.TestValue',
            field_names=['non_existent_field']))

# Incorrect types.
with self.assertRaisesOpError('Incompatible type for field double_value.'):
    self.evaluate(
        self._encode_module.encode_proto(
            sizes=[[1]],
            values=[np.array([[0.0]], dtype=np.int32)],
            message_type='tensorflow.contrib.proto.TestValue',
            field_names=['double_value']))

# Incorrect shapes of sizes.
for sizes_value in 1, np.array([[[0, 0]]]):
    with self.assertRaisesOpError(
        r'sizes should be batch_size \+ \[len\(field_names\)\]'):
        if context.executing_eagerly():
            self.evaluate(
                self._encode_module.encode_proto(
                    sizes=sizes_value,
                    values=[np.array([[0.0]])],
                    message_type='tensorflow.contrib.proto.TestValue',
                    field_names=['double_value']))
        else:
            with self.cached_session():
                sizes = array_ops.placeholder(dtypes.int32)
                values = array_ops.placeholder(dtypes.float64)
                self._encode_module.encode_proto(
                    sizes=sizes,
                    values=[values],
                    message_type='tensorflow.contrib.proto.TestValue',
                    field_names=['double_value']).eval(feed_dict={
                        sizes: sizes_value,
                        values: [[0.0]]
                    })

    # Inconsistent shapes of values.
with self.assertRaisesOpError('Values must match up to the last dimension'):
    if context.executing_eagerly():
        self.evaluate(
            self._encode_module.encode_proto(
                sizes=[[1, 1]],
                values=[np.array([[0.0]]),
                        np.array([[0], [0]])],
                message_type='tensorflow.contrib.proto.TestValue',
                field_names=['double_value', 'int32_value']))
    else:
        with self.cached_session():
            values1 = array_ops.placeholder(dtypes.float64)
            values2 = array_ops.placeholder(dtypes.int32)
            (self._encode_module.encode_proto(
                sizes=[[1, 1]],
                values=[values1, values2],
                message_type='tensorflow.contrib.proto.TestValue',
                field_names=['double_value', 'int32_value']).eval(feed_dict={
                    values1: [[0.0]],
                    values2: [[0], [0]]
                }))
