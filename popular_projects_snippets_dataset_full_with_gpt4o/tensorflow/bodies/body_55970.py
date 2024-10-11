# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrEmptyListDefault", a=None, name="b")
    self.assertProtoEquals("""
        name: 'b' op: 'AttrEmptyListDefault'
        attr { key: 'a' value { list { } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrEmptyListDefault", a=[3], name="a")
    self.assertProtoEquals("""
        name: 'a' op: 'AttrEmptyListDefault'
        attr { key: 'a' value { list { f: 3 } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrEmptyListDefault", a=[], name="empty")
    self.assertProtoEquals("""
        name: 'empty' op: 'AttrEmptyListDefault'
        attr { key: 'a' value { list { } } }
        """, op.node_def)
