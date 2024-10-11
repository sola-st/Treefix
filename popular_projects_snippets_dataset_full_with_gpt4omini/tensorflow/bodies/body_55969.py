# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrListDefault", a=None, name="b")
    self.assertProtoEquals("""
        name: 'b' op: 'AttrListDefault'
        attr { key: 'a' value { list { i: 5 i: 15 } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrListDefault", a=[3], name="a")
    self.assertProtoEquals("""
        name: 'a' op: 'AttrListDefault'
        attr { key: 'a' value { list { i: 3 } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrListDefault", a=[], name="empty")
    self.assertProtoEquals("""
        name: 'empty' op: 'AttrListDefault'
        attr { key: 'a' value { list { } } }
        """, op.node_def)
