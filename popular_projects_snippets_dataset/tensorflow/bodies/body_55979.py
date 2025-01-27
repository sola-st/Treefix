# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "NInTwoTypeVariables", a=[1, 2], b=[True, False], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'NInTwoTypeVariables'
        input: 'n/a_0' input: 'n/a_1' input: 'n/b_0' input: 'n/b_1'
        attr { key: 'S' value { type: DT_INT32 } }
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NInTwoTypeVariables", a=[1, 2], b=[3, 4], name="o")
    self.assertProtoEquals("""
        name: 'o' op: 'NInTwoTypeVariables'
        input: 'o/a_0' input: 'o/a_1' input: 'o/b_0' input: 'o/b_1'
        attr { key: 'S' value { type: DT_INT32 } }
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NInTwoTypeVariables",
        a=[self.Tensor(dtypes.int32, name="q")],
        b=[self.Tensor(dtypes.string, name="r")],
        name="p")
    self.assertProtoEquals("""
        name: 'p' op: 'NInTwoTypeVariables' input: 'q' input: 'r'
        attr { key: 'S' value { type: DT_INT32 } }
        attr { key: 'T' value { type: DT_STRING } }
        attr { key: 'N' value { i: 1 } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NInTwoTypeVariables", a=[1, 2, 3], b=["5"])
    self.assertEqual(str(cm.exception),
                     "List argument 'b' to 'NInTwoTypeVariables' Op "
                     "with length 1 "
                     "must match length 3 of argument 'a'.")
