# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = test_ops.default_attrs()
self.assertEqual(op.get_attr("string_val"), b"abc")
self.assertEqual(op.get_attr("string_list_val"), [b"abc", b""])
self.assertEqual(op.get_attr("int_val"), 123)
self.assertEqual(op.get_attr("int_list_val"), [1, 2, 3])
self.assertEqual(op.get_attr("float_val"), 10.0)
self.assertEqual(op.get_attr("float_list_val"), [10.0])
self.assertEqual(op.get_attr("bool_val"), True)
self.assertEqual(op.get_attr("bool_list_val"), [True, False])
self.assertEqual(op.get_attr("shape_val"),
                 tensor_shape.as_shape([2, 1]).as_proto())
self.assertEqual(op.get_attr("shape_list_val"),
                 [tensor_shape.as_shape([]).as_proto(),
                  tensor_shape.as_shape([1]).as_proto()])
self.assertEqual(op.get_attr("tensor_val"),
                 tensor_util.make_tensor_proto(1, dtypes.int32))
self.assertEqual(op.get_attr("tensor_list_val"),
                 [tensor_util.make_tensor_proto(1, dtypes.int32)])

type_val = op.get_attr("type_val")
# First check that type_val is a DType, because the assertEqual will work
# no matter what since DType overrides __eq__
self.assertIsInstance(type_val, dtypes.DType)
self.assertEqual(type_val, dtypes.int32)

type_list_val = op.get_attr("type_list_val")
self.assertTrue(all(isinstance(x, dtypes.DType) for x in type_list_val))
self.assertEqual(type_list_val, [dtypes.int32, dtypes.float32])

@function.Defun(dtypes.float32, func_name="MyFunc")
def func(x):
    exit(x)

op = test_ops.func_attr(func)
self.assertEqual(op.get_attr("f"),
                 attr_value_pb2.NameAttrList(name="MyFunc"))

# Try fetching missing attr
with self.assertRaisesRegex(
    ValueError, "Operation 'FuncAttr' has no attr named 'FakeAttr'."):
    op.get_attr("FakeAttr")
