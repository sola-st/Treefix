# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("RefOut", T=dtypes.bool, name="o")
    self.assertEqual(dtypes.bool_ref, out.dtype)
    self.assertProtoEquals("""
        name: 'o' op: 'RefOut'
        attr { key: 'T' value { type: DT_BOOL } }
        """, out.op.node_def)

    op = op_def_library.apply_op("RefIn", a=out, name="i")
    self.assertProtoEquals("""
        name: 'i' op: 'RefIn' input: 'o'
        attr { key: 'T' value { type: DT_BOOL } }
        attr { key: "_class" value { list { s: "loc:@o" } } }
        """, op.node_def)

    # Can pass ref to non-ref input.
    out = op_def_library.apply_op("RefOut", T=dtypes.int32, name="r")
    out = op_def_library.apply_op("Simple", a=out, name="s")
    self.assertProtoEquals("""
        name: 's' op: 'Simple' input: 'r'
        """, out.op.node_def)

    # Can't pass non-ref to ref input.
    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("RefIn", a=2)
    self.assertEqual(
        str(cm.exception),
        "'RefIn' Op requires that input 'a' be a mutable tensor " +
        "(e.g.: a tf.Variable)")

    input_a = op_def_library.apply_op("RefOut", T=dtypes.int32, name="t")
    input_b = op_def_library.apply_op("RefOut", T=dtypes.int32, name="u")
    op = op_def_library.apply_op("TwoRefsIn", a=input_a, b=input_b, name="v")
    # NOTE(mrry): The order of colocation constraints is an implementation
    # detail.
    self.assertProtoEquals("""
        name: 'v' op: 'TwoRefsIn' input: 't' input: 'u'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: "_class" value { list { s: "loc:@t" s: "loc:@u" } } }
        """, op.node_def)
