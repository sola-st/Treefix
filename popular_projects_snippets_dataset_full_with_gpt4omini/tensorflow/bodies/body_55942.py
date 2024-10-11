# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("Restrict", a="foo", name="g")
    self.assertEqual(dtypes.string, out.dtype)
    self.assertProtoEquals("""
        name: 'g' op: 'Restrict' input: 'g/a'
        attr { key: 'T' value { type: DT_STRING } }
        """, out.op.node_def)

    out = op_def_library.apply_op("Restrict", a=True, name="h")
    self.assertEqual(dtypes.bool, out.dtype)
    self.assertProtoEquals("""
        name: 'h' op: 'Restrict' input: 'h/a'
        attr { key: 'T' value { type: DT_BOOL } }
        """, out.op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Restrict", a=17)
    self.assertEqual(str(cm.exception),
                     "Value passed to parameter 'a' has DataType int32 "
                     "not in list of allowed values: string, bool")
