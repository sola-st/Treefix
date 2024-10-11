# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "NInTwice", a=[1, 2], b=["one", "two"], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'NInTwice'
        input: 'n/a_0' input: 'n/a_1' input: 'n/b_0' input: 'n/b_1'
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op("NInTwice", a=[], b=[], name="o")
    self.assertProtoEquals("""
        name: 'o' op: 'NInTwice' attr { key: 'N' value { i: 0 } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NInTwice", a=[1, 2, 3], b=["too short"])
    self.assertEqual(str(cm.exception),
                     "List argument 'b' to 'NInTwice' Op "
                     "with length 1 must match "
                     "length 3 of argument 'a'.")
