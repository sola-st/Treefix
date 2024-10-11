# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
test_case = test_example_pb2.TestCase()
test_case.values.add()  # No fields specified, so we get all defaults.
test_case.shapes.append(1)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "double_value_with_default"
field.dtype = types_pb2.DT_DOUBLE
field.value.double_value.append(1.0)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "float_value_with_default"
field.dtype = types_pb2.DT_FLOAT
field.value.float_value.append(2.0)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "int64_value_with_default"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(3)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "sfixed64_value_with_default"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(11)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "sint64_value_with_default"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(13)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "uint64_value_with_default"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(4)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "fixed64_value_with_default"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(6)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "int32_value_with_default"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(5)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "sfixed32_value_with_default"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(10)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "sint32_value_with_default"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(12)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "uint32_value_with_default"
field.dtype = types_pb2.DT_UINT32
field.value.uint32_value.append(9)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "fixed32_value_with_default"
field.dtype = types_pb2.DT_UINT32
field.value.uint32_value.append(7)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "bool_value_with_default"
field.dtype = types_pb2.DT_BOOL
field.value.bool_value.append(True)
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "string_value_with_default"
field.dtype = types_pb2.DT_STRING
field.value.string_value.append("a")
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "bytes_value_with_default"
field.dtype = types_pb2.DT_STRING
field.value.string_value.append("a longer default string")
test_case.sizes.append(0)
field = test_case.fields.add()
field.name = "enum_value_with_default"
field.dtype = types_pb2.DT_INT32
field.value.enum_value.append(test_example_pb2.Color.GREEN)
exit(test_case)
