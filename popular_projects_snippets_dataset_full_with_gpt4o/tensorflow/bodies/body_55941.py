# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("Binary", a=8, b=9, name="b")
    self.assertEqual(dtypes.int32, out.dtype)
    self.assertProtoEquals("""
        name: 'b' op: 'Binary' input: 'b/a' input: 'b/b'
        attr { key: 'T' value { type: DT_INT32 } }
        """, out.op.node_def)

    out = op_def_library.apply_op("Binary", a="left", b="right", name="c")
    self.assertEqual(dtypes.string, out.dtype)
    self.assertProtoEquals("""
        name: 'c' op: 'Binary' input: 'c/a' input: 'c/b'
        attr { key: 'T' value { type: DT_STRING } }
        """, out.op.node_def)

    with self.assertRaises(TypeError):
        op_def_library.apply_op("Binary", a="left", b=12)

    with self.assertRaises(TypeError):
        op_def_library.apply_op(
            "Binary", a=self.Tensor(dtypes.string), b=self.Tensor(dtypes.int32))
