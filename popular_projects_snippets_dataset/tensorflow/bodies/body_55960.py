# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrMin", a=12, name="s")
    self.assertProtoEquals("""
        name: 's' op: 'AttrMin' attr { key: 'a' value { i: 12 } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("AttrMin", a=2)
    self.assertEqual(str(cm.exception),
                     "Attr 'a' of 'AttrMin' Op passed 2 less than minimum 5.")
