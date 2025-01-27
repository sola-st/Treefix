# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2 = op_def_library.apply_op(
        "NPolymorphicOut", N=2, T=dtypes.int32, name="n")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertProtoEquals("""
        name: 'n' op: 'NPolymorphicOut'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 2 } }
        """, out1.op.node_def)

    out1, out2, out3 = op_def_library.apply_op(
        "NPolymorphicOut", T=dtypes.string, N=3, name="o")
    self.assertEqual(dtypes.string, out1.dtype)
    self.assertEqual(dtypes.string, out2.dtype)
    self.assertEqual(dtypes.string, out3.dtype)
    self.assertProtoEquals("""
        name: 'o' op: 'NPolymorphicOut'
        attr { key: 'T' value { type: DT_STRING } }
        attr { key: 'N' value { i: 3 } }
        """, out3.op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NPolymorphicOut", N=1, T=dtypes.string)
    self.assertEqual(str(cm.exception),
                     "Attr 'N' of 'NPolymorphicOut' Op "
                     "passed 1 less than minimum 2.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicOut", N=3, T=[dtypes.string])
    self.assertEqual(
        str(cm.exception),
        "Expected DataType for argument 'T' not [tf.string].")
