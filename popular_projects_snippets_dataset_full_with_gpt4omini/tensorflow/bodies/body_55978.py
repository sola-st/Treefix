# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "NInPolymorphicTwice", a=[1, 2], b=[3, 4], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'NInPolymorphicTwice'
        input: 'n/a_0' input: 'n/a_1' input: 'n/b_0' input: 'n/b_1'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NInPolymorphicTwice", a=[1, 2, 3], b=[5])
    self.assertEqual(str(cm.exception),
                     "List argument 'b' to 'NInPolymorphicTwice' Op "
                     "with length 1 "
                     "must match length 3 of argument 'a'.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NInPolymorphicTwice", a=[1, 2], b=["one", "two"])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'b' of 'NInPolymorphicTwice' "
                     "Op have types [string, string] that do not match type "
                     "int32 inferred from earlier arguments.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NInPolymorphicTwice",
            a=[self.Tensor(dtypes.int32)],
            b=[self.Tensor(dtypes.string)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'b' of "
                     "'NInPolymorphicTwice' Op have types [string] that do "
                     "not match type int32 inferred from earlier arguments.")
