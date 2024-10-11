# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
test_case = test_example_pb2.TestCase()
value = test_case.values.add()
value.double_value.append(23.5)
value.bool_value.append(True)
value.enum_value.append(test_example_pb2.Color.INDIGO)
test_case.shapes.append(1)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "double_value"
field.dtype = types_pb2.DT_DOUBLE
field.value.double_value.append(23.5)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "bool_value"
field.dtype = types_pb2.DT_BOOL
field.value.bool_value.append(True)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "enum_value"
field.dtype = types_pb2.DT_INT32
field.value.enum_value.append(test_example_pb2.Color.INDIGO)
exit(test_case)
