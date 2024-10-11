# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out1, out2 = op_def_library.apply_op(
        "OutTypeListRestrict", t=[dtypes.bool, dtypes.string], name="u")
    self.assertEqual(dtypes.bool, out1.dtype)
    self.assertEqual(dtypes.string, out2.dtype)
    self.assertProtoEquals("""
        name: 'u' op: 'OutTypeListRestrict'
        attr { key: 't' value { list { type: DT_BOOL type: DT_STRING } } }
        """, out1.op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "OutTypeListRestrict", t=[dtypes.string, dtypes.int32])
    self.assertEqual(str(cm.exception),
                     "Value passed to parameter 't' has DataType int32 "
                     "not in list of allowed values: string, bool")
