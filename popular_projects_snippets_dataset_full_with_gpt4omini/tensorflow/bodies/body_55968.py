# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrDefault", a=None, name="d")
    self.assertProtoEquals("""
        name: 'd' op: 'AttrDefault' attr { key: 'a' value { s: 'banana' } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrDefault", a="kiwi", name="c")
    self.assertProtoEquals("""
        name: 'c' op: 'AttrDefault' attr { key: 'a' value { s: 'kiwi' } }
        """, op.node_def)
