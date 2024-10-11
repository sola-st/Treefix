# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "AttrShapeList", a=[[3, 2], [6, 5, 4]], name="sl")
    self.assertProtoEquals("""
        name: 'sl' op: 'AttrShapeList'
        attr { key: 'a' value { list {
          shape { dim { size: 3 } dim { size: 2 } }
          shape { dim { size: 6 } dim { size: 5 } dim { size: 4 } } } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrShapeList", a=[], name="esl")
    self.assertProtoEquals("""
        name: 'esl' op: 'AttrShapeList' attr { key: 'a' value { list { } } }
        """, op.node_def)
