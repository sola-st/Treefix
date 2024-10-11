# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("Attr", a=12, name="t")
    self.assertProtoEquals("""
        name: 't' op: 'Attr' attr { key: 'a' value { i: 12 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "Attr", a=tensor_shape.Dimension(13), name="u")
    self.assertProtoEquals("""
        name: 'u' op: 'Attr' attr { key: 'a' value { i: 13 } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Attr", a="bad")
    self.assertEqual(str(cm.exception),
                     "Expected int for argument 'a' not 'bad'.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Attr", a=[12])
    self.assertEqual(str(cm.exception),
                     "Expected int for argument 'a' not [12].")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Attr", a=None)
    self.assertEqual(str(cm.exception),
                     "Expected int for argument 'a' not None.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Attr")
    self.assertEqual(
        str(cm.exception), "No argument found for attr a for "
        "Attr")
