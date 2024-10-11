# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
test_case = test_example_pb2.TestCase()
value = test_case.values.add()
value.sint32_value.append(2147483647)
value.sfixed32_value.append(2147483647)
value.int32_value.append(2147483647)
value.fixed32_value.append(4294967295)
value.uint32_value.append(4294967295)
test_case.shapes.append(1)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "sint32_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(2147483647)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "sfixed32_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(2147483647)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "int32_value"
field.dtype = types_pb2.DT_INT64
field.value.int64_value.append(2147483647)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "fixed32_value"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(4294967295)
test_case.sizes.append(1)
field = test_case.fields.add()
field.name = "uint32_value"
field.dtype = types_pb2.DT_UINT64
field.value.uint64_value.append(4294967295)
exit(test_case)
