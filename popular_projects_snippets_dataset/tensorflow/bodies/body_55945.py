# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out, = op_def_library.apply_op(
        "OutTypeList", T=[dtypes.float32], name="x")
    self.assertEqual(dtypes.float32, out.dtype)
    self.assertProtoEquals("""
        name: 'x' op: 'OutTypeList'
        attr { key: 'T' value { list { type: DT_FLOAT } } }
        """, out.op.node_def)

    out1, out2 = op_def_library.apply_op(
        "OutTypeList", T=[dtypes.int32, dtypes.bool], name="w")
    self.assertEqual(dtypes.int32, out1.dtype)
    self.assertEqual(dtypes.bool, out2.dtype)
    self.assertProtoEquals("""
        name: 'w' op: 'OutTypeList'
        attr { key: 'T' value { list { type: DT_INT32 type: DT_BOOL } } }
        """, out1.op.node_def)

    out = op_def_library.apply_op("OutTypeList", T=[], name="empty")
    self.assertEqual([], out)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("OutTypeList", T=dtypes.int32)
    self.assertEqual(
        str(cm.exception), "Expected list for attr T, obtained "
        "DType instead.")
