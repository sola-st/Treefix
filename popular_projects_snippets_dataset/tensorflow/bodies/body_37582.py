# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
test_case = test_example_pb2.TestCase()
value = test_case.values.add()
value.double_value.append(-1.7976931348623158e+308)
value.double_value.append(2.2250738585072014e-308)
value.double_value.append(1.7976931348623158e+308)
value.float_value.append(-3.402823466e+38)
value.float_value.append(1.175494351e-38)
value.float_value.append(3.402823466e+38)
value.int64_value.append(-9223372036854775808)
value.int64_value.append(9223372036854775807)
value.sfixed64_value.append(-9223372036854775808)
value.sfixed64_value.append(9223372036854775807)
value.sint64_value.append(-9223372036854775808)
value.sint64_value.append(9223372036854775807)
value.uint64_value.append(0)
value.uint64_value.append(18446744073709551615)
value.fixed64_value.append(0)
value.fixed64_value.append(18446744073709551615)
value.int32_value.append(-2147483648)
value.int32_value.append(2147483647)
value.sfixed32_value.append(-2147483648)
value.sfixed32_value.append(2147483647)
value.sint32_value.append(-2147483648)
value.sint32_value.append(2147483647)
value.uint32_value.append(0)
value.uint32_value.append(4294967295)
value.fixed32_value.append(0)
value.fixed32_value.append(4294967295)
value.bool_value.append(False)
value.bool_value.append(True)
value.string_value.append("")
value.string_value.append("I refer to the infinite.")
test_case.shapes.append(1)
test_case.sizes.append(3)
field = test_case.fields.add()
field.name = "double_value"
field.dtype = types_pb2.DT_DOUBLE
field.value.double_value.append(-1.7976931348623158e+308)
field.value.double_value.append(2.2250738585072014e-308)
field.value.double_value.append(1.7976931348623158e+308)
test_case.sizes.append(3)
field = test_case.fields.add()
field.name = "float_value"
field.dtype = types_pb2.DT_FLOAT
field.value.float_value.append(-3.402823466e+38)
field.value.float_value.append(1.175494351e-38)
field.value.float_value.append(3.402823466e+38)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "int64_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(-9223372036854775808)
field.value.int64_value.append(9223372036854775807)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "sfixed64_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(-9223372036854775808)
field.value.int64_value.append(9223372036854775807)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "sint64_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(-9223372036854775808)
field.value.int64_value.append(9223372036854775807)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "uint64_value"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(0)
field.value.uint64_value.append(18446744073709551615)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "fixed64_value"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(0)
field.value.uint64_value.append(18446744073709551615)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "int32_value"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(-2147483648)
field.value.int32_value.append(2147483647)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "sfixed32_value"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(-2147483648)
field.value.int32_value.append(2147483647)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "sint32_value"
field.dtype = types_pb2.DT_INT32
field.value.int32_value.append(-2147483648)
field.value.int32_value.append(2147483647)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "uint32_value"
field.dtype = types_pb2.DT_UINT32
field.value.uint32_value.append(0)
field.value.uint32_value.append(4294967295)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "fixed32_value"
field.dtype = types_pb2.DT_UINT32
field.value.uint32_value.append(0)
field.value.uint32_value.append(4294967295)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "bool_value"
field.dtype = types_pb2.DT_BOOL
field.value.bool_value.append(False)
field.value.bool_value.append(True)
test_case.sizes.append(2)
field = test_case.fields.add()
field.name = "string_value"
field.dtype = types_pb2.DT_STRING
field.value.string_value.append("")
field.value.string_value.append("I refer to the infinite.")
exit(test_case)
