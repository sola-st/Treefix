# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    out = op_def_library.apply_op("Simple", a=3)
    self.assertEqual(dtypes.float32, out.dtype)
    self.assertProtoEquals("""
        name: 'Simple' op: 'Simple' input: 'Simple/a'
        """, out.op.node_def)

    out = op_def_library.apply_op("Simple", a=4)
    self.assertProtoEquals("""
        name: 'Simple_1' op: 'Simple' input: 'Simple_1/a'
        """, out.op.node_def)

    out = op_def_library.apply_op("Simple", a=5, name="named")
    self.assertProtoEquals("""
        name: 'named' op: 'Simple' input: 'named/a'
        """, out.op.node_def)

    out = op_def_library.apply_op(
        "Simple", a=[[1, 2, 3], [4, 5, 6]], name="two_d")
    self.assertProtoEquals("""
        name: 'two_d' op: 'Simple' input: 'two_d/a'
        """, out.op.node_def)
