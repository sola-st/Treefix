# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("Polymorphic", a=7, name="p")
    self.assertEqual(dtypes.int32, out.dtype)
    self.assertProtoEquals("""
        name: 'p' op: 'Polymorphic' input: 'p/a'
        attr { key: 'T' value { type: DT_INT32 } }
        """, out.op.node_def)

    out = op_def_library.apply_op("Polymorphic", a="s", name="q")
    self.assertEqual(dtypes.string, out.dtype)
    self.assertProtoEquals("""
        name: 'q' op: 'Polymorphic' input: 'q/a'
        attr { key: 'T' value { type: DT_STRING } }
        """, out.op.node_def)

    out = op_def_library.apply_op("Polymorphic", a=["s", "t", "u"], name="r")
    self.assertEqual(dtypes.string, out.dtype)
    self.assertProtoEquals("""
        name: 'r' op: 'Polymorphic' input: 'r/a'
        attr { key: 'T' value { type: DT_STRING } }
        """, out.op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Polymorphic", a="s", T=dtypes.string)
    self.assertEqual(
        str(cm.exception),
        "Should not specify value for inferred attr 'T' for "
        "Polymorphic.")
