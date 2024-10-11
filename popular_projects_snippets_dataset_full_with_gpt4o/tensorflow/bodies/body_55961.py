# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrListMin", a=[1, 2], name="r")
    self.assertProtoEquals("""
        name: 'r' op: 'AttrListMin'
        attr { key: 'a' value { list { i: 1 i: 2 } } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("AttrListMin", a=[17])
    self.assertEqual(str(cm.exception),
                     "Attr 'a' of 'AttrListMin' Op "
                     "passed list of length 1 less than minimum 2.")
