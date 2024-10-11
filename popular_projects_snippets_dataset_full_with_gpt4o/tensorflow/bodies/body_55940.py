# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("PolymorphicDefaultOut", T=None, name="p")
    self.assertEqual(dtypes.string, out.dtype)
    self.assertProtoEquals("""
        name: 'p' op: 'PolymorphicDefaultOut'
        attr { key: 'T' value { type: DT_STRING } }
        """, out.op.node_def)

    out = op_def_library.apply_op(
        "PolymorphicDefaultOut", T=dtypes.bool, name="q")
    self.assertEqual(dtypes.bool, out.dtype)
    self.assertProtoEquals("""
        name: 'q' op: 'PolymorphicDefaultOut'
        attr { key: 'T' value { type: DT_BOOL } }
        """, out.op.node_def)
