# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2 = op_def_library.apply_op("NIntsOut", N=2, name="n")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertProtoEquals("""
        name: 'n' op: 'NIntsOut' attr { key: 'N' value { i: 2 } }
        """, out1.op.node_def)

    out1, out2, out3, out4, out5 = op_def_library.apply_op(
        "NIntsOut", N=5, name="o")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertEqual(dtypes.int32, out3.dtype)
    self.assertEqual(dtypes.int32, out4.dtype)
    self.assertEqual(dtypes.int32, out5.dtype)
    self.assertProtoEquals("""
        name: 'o' op: 'NIntsOut' attr { key: 'N' value { i: 5 } }
        """, out5.op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NIntsOut", N=1)
    self.assertEqual(
        str(cm.exception),
        "Attr 'N' of 'NIntsOut' Op passed 1 less than minimum 2.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NIntsOut", N=[3])
    self.assertEqual(str(cm.exception),
                     "Expected int for argument 'N' not [3].")
