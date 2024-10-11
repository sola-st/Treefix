# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
"""Compare protos of type TestValue.

    Args:
      batch_shape: the shape of the input tensor of serialized messages.
      sizes: int matrix of repeat counts returned by decode_proto
      fields: list of test_example_pb2.FieldSpec (types and expected values)
      field_dict: map from field names to decoded numpy tensors of values
    """

# Check that expected values match.
for field in fields:
    values = field_dict[field.name]
    self.assertEqual(dtypes.as_dtype(values.dtype), field.dtype)

    if 'ext_value' in field.name:
        fd = test_example_pb2.PrimitiveValue()
    else:
        fd = field.value.DESCRIPTOR.fields_by_name[field.name]

    # Values has the same shape as the input plus an extra
    # dimension for repeats.
    self.assertEqual(list(values.shape)[:-1], batch_shape)

    # Nested messages are represented as TF strings, requiring
    # some special handling.
    if field.name == 'message_value' or 'ext_value' in field.name:
        vs = []
        for buf in values.flat:
            msg = test_example_pb2.PrimitiveValue()
            msg.ParseFromString(buf)
            vs.append(msg)
        if 'ext_value' in field.name:
            evs = field.value.Extensions[test_example_pb2.ext_value]
        else:
            evs = getattr(field.value, field.name)
        if len(vs) != len(evs):
            self.fail('Field %s decoded %d outputs, expected %d' %
                      (fd.name, len(vs), len(evs)))
        for v, ev in zip(vs, evs):
            self.assertEqual(v, ev)
        continue

    tf_type_to_primitive_value_field = {
        dtypes.bool:
            'bool_value',
        dtypes.float32:
            'float_value',
        dtypes.float64:
            'double_value',
        dtypes.int8:
            'int8_value',
        dtypes.int32:
            'int32_value',
        dtypes.int64:
            'int64_value',
        dtypes.string:
            'string_value',
        dtypes.uint8:
            'uint8_value',
        dtypes.uint32:
            'uint32_value',
        dtypes.uint64:
            'uint64_value',
    }
    if field.name in ['enum_value', 'enum_value_with_default']:
        tf_field_name = 'enum_value'
    else:
        tf_field_name = tf_type_to_primitive_value_field.get(field.dtype)
    if tf_field_name is None:
        self.fail('Unhandled tensorflow type %d' % field.dtype)

    self._compareValues(fd, values.flat,
                        getattr(field.value, tf_field_name))
