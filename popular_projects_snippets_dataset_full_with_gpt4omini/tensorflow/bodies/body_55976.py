# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "NPolymorphicRestrictIn", a=["foo", "bar"], name="p")
    self.assertProtoEquals("""
        name: 'p' op: 'NPolymorphicRestrictIn' input: 'p/a_0' input: 'p/a_1'
        attr { key: 'T' value { type: DT_STRING } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NPolymorphicRestrictIn", a=[False, True, False], name="b")
    self.assertProtoEquals("""
        name: 'b' op: 'NPolymorphicRestrictIn'
        input: 'b/a_0' input: 'b/a_1' input: 'b/a_2'
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: 'N' value { i: 3 } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicRestrictIn", a=[1, 2])
    self.assertEqual(
        str(cm.exception),
        "Value passed to parameter 'a' has DataType int32 not in "
        "list of allowed values: string, bool")
