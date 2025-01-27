# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2 = op_def_library.apply_op(
        "NPolymorphicOutDefault", N=None, T=None, name="r")
    self.assertEqual(dtypes.bool, out1.dtype)
    self.assertEqual(dtypes.bool, out2.dtype)
    self.assertProtoEquals("""
        name: 'r' op: 'NPolymorphicOutDefault'
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: 'N' value { i: 2 } }
        """, out1.op.node_def)

    out1, out2, out3 = op_def_library.apply_op(
        "NPolymorphicOutDefault", N=3, T=None, name="s")
    self.assertEqual(dtypes.bool, out1.dtype)
    self.assertEqual(dtypes.bool, out2.dtype)
    self.assertEqual(dtypes.bool, out3.dtype)
    self.assertProtoEquals("""
        name: 's' op: 'NPolymorphicOutDefault'
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: 'N' value { i: 3 } }
        """, out1.op.node_def)

    out1, out2 = op_def_library.apply_op(
        "NPolymorphicOutDefault", N=None, T=dtypes.int32, name="t")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertProtoEquals("""
        name: 't' op: 'NPolymorphicOutDefault'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 2 } }
        """, out1.op.node_def)

    out1, out2, out3 = op_def_library.apply_op(
        "NPolymorphicOutDefault", N=3, T=dtypes.int32, name="u")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertEqual(dtypes.int32, out3.dtype)
    self.assertProtoEquals("""
        name: 'u' op: 'NPolymorphicOutDefault'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 3 } }
        """, out1.op.node_def)
