# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    # Give an input whose type has no obvious output type.
    op = op_def_library.apply_op("AttrTypeDefault", a=[], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'AttrTypeDefault' input: 'n/a'
        attr { key: 'T' value { type: DT_INT32 } }
        """, op.node_def)

    # Give an input whose type can be inferred as different
    # than the default.
    op = op_def_library.apply_op("AttrTypeDefault", a=[1.0], name="f")
    self.assertProtoEquals("""
        name: 'f' op: 'AttrTypeDefault' input: 'f/a'
        attr { key: 'T' value { type: DT_FLOAT } }
        """, op.node_def)
