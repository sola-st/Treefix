# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("ReservedInput", input_=7, name="x")
    self.assertProtoEquals("""
        name: 'x' op: 'ReservedInput' input: 'x/input'
        """, op.node_def)
