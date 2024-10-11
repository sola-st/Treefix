# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("NIntsIn", a=[1, 2], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'NIntsIn' input: 'n/a_0' input: 'n/a_1'
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op("NIntsIn", a=[5, 4, 3, 2, 1], name="o")
    self.assertProtoEquals("""
        name: 'o' op: 'NIntsIn'
        input: 'o/a_0' input: 'o/a_1' input: 'o/a_2' input: 'o/a_3' input: 'o/a_4'
        attr { key: 'N' value { i: 5 } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NIntsIn", a=["foo", "bar"])
    self.assertEqual(
        str(cm.exception),
        "Tensors in list passed to 'a' of 'NIntsIn' Op have types "
        "[string, string] that do not match expected type int32.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NIntsIn",
            a=[self.Tensor(dtypes.string),
               self.Tensor(dtypes.string)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NIntsIn' Op have "
                     "types [string, string] that do not match expected type "
                     "int32.")

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NIntsIn", a=[99])
    self.assertEqual(str(cm.exception),
                     "List argument 'a' to 'NIntsIn' Op "
                     "with length 1 shorter than "
                     "minimum length 2.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NIntsIn", a=[38, "bar"])
    self.assertEqual(
        str(cm.exception),
        "Tensors in list passed to 'a' of 'NIntsIn' Op have types "
        "[int32, string] that do not match expected type int32.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NIntsIn",
            a=[self.Tensor(dtypes.int32),
               self.Tensor(dtypes.string)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NIntsIn' Op "
                     "have types [int32, string] that do not match expected "
                     "type int32.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NIntsIn", a=17)
    self.assertStartsWith(str(cm.exception),
                          "Expected list for 'a' argument "
                          "to 'NIntsIn' Op, not ")
