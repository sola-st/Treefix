# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
"""Run decode tests on a batch of messages.

    Args:
      fields: list of test_example_pb2.FieldSpec (types and expected values)
      case_sizes: expected sizes array
      batch_shape: the shape of the input tensor of serialized messages
      batch: list of serialized messages
      message_type: descriptor name for messages
      message_format: format of messages, 'text' or 'binary'
      sanitize: whether to sanitize binary protobuf inputs
      force_disordered: whether to force fields encoded out of order.
    """

if force_disordered:
    # Exercise code path that handles out-of-order fields by prepending extra
    # fields with tag numbers higher than any real field. Note that this won't
    # work with sanitization because that forces reserialization using a
    # trusted decoder and encoder.
    assert not sanitize
    extra_fields = test_example_pb2.ExtraFields()
    extra_fields.string_value = 'IGNORE ME'
    extra_fields.bool_value = False
    extra_msg = extra_fields.SerializeToString()
    batch = [extra_msg + msg for msg in batch]

# Numpy silently truncates the strings if you don't specify dtype=object.
batch = np.array(batch, dtype=object)
batch = np.reshape(batch, batch_shape)

field_names = [f.name for f in fields]
output_types = [f.dtype for f in fields]

with self.cached_session() as sess:
    sizes, vtensor = self._decode_module.decode_proto(
        batch,
        message_type=message_type,
        field_names=field_names,
        output_types=output_types,
        message_format=message_format,
        sanitize=sanitize)

    vlist = sess.run([sizes] + vtensor)
    sizes = vlist[0]
    # Values is a list of tensors, one for each field.
    value_tensors = vlist[1:]

    # Check that the repeat sizes are correct.
    self.assertTrue(
        np.all(np.array(sizes.shape) == batch_shape + [len(field_names)]))

    # Check that the decoded sizes match the expected sizes.
    self.assertEqual(len(sizes.flat), len(case_sizes))
    self.assertTrue(
        np.all(sizes.flat == np.array(
            case_sizes, dtype=np.int32)))

    field_dict = dict(zip(field_names, value_tensors))

    self._compareProtos(batch_shape, sizes, fields, field_dict)
