# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "InPolymorphicTwice", a=[8], b=[3, 4, 5], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'InPolymorphicTwice'
        input: 'n/a_0' input: 'n/b_0' input: 'n/b_1' input: 'n/b_2'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 1 } }
        attr { key: 'M' value { i: 3 } }
        """, op.node_def)

    op = op_def_library.apply_op("InPolymorphicTwice", a=[8], b=[], name="o")
    self.assertProtoEquals("""
        name: 'o' op: 'InPolymorphicTwice' input: 'o/a_0'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 1 } }
        attr { key: 'M' value { i: 0 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "InPolymorphicTwice", a=[], b=[3, 4], name="p")
    self.assertProtoEquals("""
        name: 'p' op: 'InPolymorphicTwice' input: 'p/b_0' input: 'p/b_1'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 0 } }
        attr { key: 'M' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "InPolymorphicTwice", a=[], b=[3.0, 4.0], name="q")
    self.assertProtoEquals("""
        name: 'q' op: 'InPolymorphicTwice' input: 'q/b_0' input: 'q/b_1'
        attr { key: 'T' value { type: DT_FLOAT } }
        attr { key: 'N' value { i: 0 } }
        attr { key: 'M' value { i: 2 } }
        """, op.node_def)

    # Empty input lists: assume default type for T.
    op = op_def_library.apply_op(
        "InPolymorphicTwice", a=[], b=[], name="r")
    self.assertProtoEquals("""
        name: 'r' op: 'InPolymorphicTwice'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 0 } }
        attr { key: 'M' value { i: 0 } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "InPolymorphicTwice", a=[1, 2], b=["one", "two"])
    self.assertEqual(
        str(cm.exception),
        "Tensors in list passed to 'b' of 'InPolymorphicTwice' Op "
        "have types [string, string] that do not match type int32 "
        "inferred from earlier arguments.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "InPolymorphicTwice",
            a=[self.Tensor(dtypes.int32)],
            b=[self.Tensor(dtypes.string)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'b' of 'InPolymorphicTwice' "
                     "Op have types [string] that do not match type int32 "
                     "inferred from earlier arguments.")
