# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
fragments = [
    test_example_pb2.TestValue(double_value=[1.0]).SerializeToString(),
    test_example_pb2.TestValue(
        message_value=[test_example_pb2.PrimitiveValue(
            string_value='abc')]).SerializeToString(),
    test_example_pb2.TestValue(
        message_value=[test_example_pb2.PrimitiveValue(
            string_value='def')]).SerializeToString()
]
all_fields_to_parse = ['double_value', 'message_value']
field_types = {
    'double_value': dtypes.double,
    'message_value': dtypes.string,
}
# Test against all 3! permutations of fragments, and for each permutation
# test parsing all possible combination of 2 fields.
for indices in itertools.permutations(range(len(fragments))):
    proto = b''.join(fragments[i] for i in indices)
    for i in indices:
        if i == 1:
            expected_message_values = [
                test_example_pb2.PrimitiveValue(
                    string_value='abc').SerializeToString(),
                test_example_pb2.PrimitiveValue(
                    string_value='def').SerializeToString(),
            ]
            break
        if i == 2:
            expected_message_values = [
                test_example_pb2.PrimitiveValue(
                    string_value='def').SerializeToString(),
                test_example_pb2.PrimitiveValue(
                    string_value='abc').SerializeToString(),
            ]
            break

    expected_field_values = {
        'double_value': [[1.0]],
        'message_value': [expected_message_values],
    }

    for num_fields_to_parse in range(len(all_fields_to_parse)):
        for comb in itertools.combinations(
            all_fields_to_parse, num_fields_to_parse):
            parsed_values = self.evaluate(
                self._decode_module.decode_proto(
                    [proto],
                    message_type='tensorflow.contrib.proto.TestValue',
                    field_names=comb,
                    output_types=[field_types[f] for f in comb],
                    sanitize=False)).values
            self.assertLen(parsed_values, len(comb))
            for field_name, parsed in zip(comb, parsed_values):
                self.assertAllEqual(parsed, expected_field_values[field_name],
                                    'perm: {}, comb: {}'.format(indices, comb))
