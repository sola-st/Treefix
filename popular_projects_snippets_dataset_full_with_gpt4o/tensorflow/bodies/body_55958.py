# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrBool", a=True, name="t")
    self.assertProtoEquals("""
        name: 't' op: 'AttrBool' attr { key: 'a' value { b: true } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrBool", a=False, name="u")
    self.assertProtoEquals("""
        name: 'u' op: 'AttrBool' attr { key: 'a' value { b: false } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("AttrBool", a=0)
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not 0.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("AttrBool", a=1)
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not 1.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("AttrBool", a=[])
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not [].")
