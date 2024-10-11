# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "TypeListTwice", a=["foo", True], b=["bar", False], name="z")
    self.assertProtoEquals("""
        name: 'z' op: 'TypeListTwice'
        input: 'z/a_0' input: 'z/a_1' input: 'z/b_0' input: 'z/b_1'
        attr { key: 'T' value { list { type: DT_STRING type: DT_BOOL } } }
        """, op.node_def)

    op = op_def_library.apply_op("TypeListTwice", a=[], b=[], name="empty")
    self.assertProtoEquals("""
        name: 'empty' op: 'TypeListTwice' attr { key: 'T' value { list { } } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("TypeListTwice", a=["foo", True], b=["bar", 6])
    self.assertEqual(str(cm.exception),
                     "Input 'b' of 'TypeListTwice' Op has type list of "
                     "string, int32 that does not match type list "
                     "string, bool of argument 'a'.")
