# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2, out3 = op_def_library.apply_op(
        "NIntsOutDefault", N=None, name="z")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertEqual(dtypes.int32, out3.dtype)
    self.assertProtoEquals("""
        name: 'z' op: 'NIntsOutDefault' attr { key: 'N' value { i: 3 } }
        """, out1.op.node_def)

    out1, out2 = op_def_library.apply_op("NIntsOutDefault", N=2, name="y")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.int32, out2.dtype)
    self.assertProtoEquals("""
        name: 'y' op: 'NIntsOutDefault' attr { key: 'N' value { i: 2 } }
        """, out2.op.node_def)
