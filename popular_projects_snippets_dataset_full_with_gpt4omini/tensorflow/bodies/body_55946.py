# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "TypeListRestrict", a=["foo", False], name="v")
    self.assertProtoEquals("""
        name: 'v' op: 'TypeListRestrict' input: 'v/a_0' input: 'v/a_1'
        attr { key: 'T' value { list { type: DT_STRING type: DT_BOOL } } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("TypeListRestrict", a=[True, 12])
    self.assertEqual(str(cm.exception),
                     "Value passed to parameter 'a' has DataType int32 "
                     "not in list of allowed values: string, bool")
