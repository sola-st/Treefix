# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("PolymorphicOut", T=dtypes.int32, name="p")
    self.assertEqual(dtypes.int32, out.dtype)
    self.assertProtoEquals("""
        name: 'p' op: 'PolymorphicOut'
        attr { key: 'T' value { type: DT_INT32 } }
        """, out.op.node_def)

    out = op_def_library.apply_op("PolymorphicOut", T=dtypes.bool, name="q")
    self.assertEqual(dtypes.bool, out.dtype)
    self.assertProtoEquals("""
        name: 'q' op: 'PolymorphicOut'
        attr { key: 'T' value { type: DT_BOOL } }
        """, out.op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("PolymorphicOut")
    self.assertEqual(
        str(cm.exception), "No argument found for attr T for PolymorphicOut")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("PolymorphicOut", T=None)
    self.assertEqual(str(cm.exception),
                     "Expected DataType for argument 'T' not None.")
