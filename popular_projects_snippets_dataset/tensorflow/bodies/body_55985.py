# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2, out3 = op_def_library.apply_op(
        "NPolymorphicRestrictOut", N=3, T=dtypes.bool, name="u")
    self.assertEqual(dtypes.bool, out1.dtype)
    self.assertEqual(dtypes.bool, out2.dtype)
    self.assertEqual(dtypes.bool, out3.dtype)
    self.assertProtoEquals("""
        name: 'u' op: 'NPolymorphicRestrictOut'
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: 'N' value { i: 3 } }
        """, out1.op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicRestrictOut", N=2, T=dtypes.int32)
    self.assertEqual(str(cm.exception),
                     "Value passed to parameter 'T' has DataType int32 "
                     "not in list of allowed values: string, bool")
