# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrFloat", a=1.2, name="t")
    self.assertProtoEquals("""
        name: 't' op: 'AttrFloat' attr { key: 'a' value { f: 1.2 } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrFloat", a=12, name="u")
    self.assertProtoEquals("""
        name: 'u' op: 'AttrFloat' attr { key: 'a' value { f: 12 } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("AttrFloat", a="bad")
    self.assertEqual(str(cm.exception),
                     "Expected float for argument 'a' not 'bad'.")
