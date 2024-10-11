# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrPartialShape", a=[5], name="s1")
    self.assertProtoEquals("""
        name: 's1' op: 'AttrPartialShape'
        attr { key: 'a' value { shape { dim { size: 5 } } } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "AttrPartialShape", a=(4, None, 2), name="s2")
    self.assertProtoEquals("""
        name: 's2' op: 'AttrPartialShape'
        attr { key: 'a' value {
          shape { dim { size: 4 } dim { size: -1 } dim { size: 2 } } } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "AttrPartialShape", a=tensor_shape.TensorShape([3, None]), name="s3")
    self.assertProtoEquals("""
        name: 's3' op: 'AttrPartialShape'
        attr { key: 'a' value {
          shape { dim { size: 3 } dim { size: -1 } } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrPartialShape", a=[], name="s4")
    self.assertProtoEquals("""
        name: 's4' op: 'AttrPartialShape'
        attr { key: 'a' value { shape { } } }
        """, op.node_def)

    shape = tensor_shape_pb2.TensorShapeProto()
    shape.dim.add().size = -1
    shape.dim.add().size = 3
    op = op_def_library.apply_op("AttrPartialShape", a=shape, name="s5")
    self.assertProtoEquals("""
        name: 's5' op: 'AttrPartialShape'
        attr { key: 'a' value {
          shape { dim { size: -1 } dim { size: 3 } } } }
        """, op.node_def)

    # TODO(ebrevdo): Re-enable once we stop promoting scalars to shapes.
    # with self.assertRaises(TypeError) as cm:
    #   op_def_library.apply_op("AttrPartialShape", a=5)
    # self.assertEqual(str(cm.exception),
    #                  "Don't know how to convert 5 to a TensorShapeProto for"
    #                  " argument 'a'")

    with self.assertRaises(TypeError):
        op_def_library.apply_op("AttrPartialShape", a="ABC")
