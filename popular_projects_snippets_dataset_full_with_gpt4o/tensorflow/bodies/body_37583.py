# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
test_case = test_example_pb2.TestCase()
value = test_case.values.add()
message_value = value.message_value.add()
message_value.double_value = 23.5
test_case.shapes.append(1)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "message_value"
field.dtype = types_pb2.DT_STRING
message_value = field.value.message_value.add()
message_value.double_value = 23.5
exit(test_case)
