# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    # Give an input whose type can be inferred as different
    # than the default.
    op = op_def_library.apply_op(
        "AttrListTypeDefault", a=[1.0], b=[2.0], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'AttrListTypeDefault' input: 'n/a_0' input: 'n/b_0'
        attr { key: 'T' value { type: DT_FLOAT } }
        attr { key: 'N' value { i: 1 } }
        """, op.node_def)
