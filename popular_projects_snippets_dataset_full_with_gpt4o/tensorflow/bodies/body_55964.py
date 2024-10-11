# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrShape", a=[5], name="s1")
    self.assertProtoEquals("""
        name: 's1' op: 'AttrShape'
        attr { key: 'a' value { shape { dim { size: 5 } } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrShape", a=(4, 3, 2), name="s2")
    self.assertProtoEquals("""
        name: 's2' op: 'AttrShape'
        attr { key: 'a' value {
          shape { dim { size: 4 } dim { size: 3 } dim { size: 2 } } } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "AttrShape", a=tensor_shape.TensorShape([3, 2]), name="s3")
    self.assertProtoEquals("""
        name: 's3' op: 'AttrShape'
        attr { key: 'a' value {
          shape { dim { size: 3 } dim { size: 2 } } } }
        """, op.node_def)

    op = op_def_library.apply_op("AttrShape", a=[], name="s4")
    self.assertProtoEquals("""
        name: 's4' op: 'AttrShape' attr { key: 'a' value { shape { } } }
        """, op.node_def)

    shape = tensor_shape_pb2.TensorShapeProto()
    shape.dim.add().size = 6
    shape.dim.add().size = 3
    op = op_def_library.apply_op("AttrShape", a=shape, name="s5")
    self.assertProtoEquals("""
        name: 's5' op: 'AttrShape'
        attr { key: 'a' value { shape { dim { size: 6 } dim { size: 3 } } } }
        """, op.node_def)

    # TODO(josh11b): Re-enable this test once we stop promoting scalars to
    # shapes.
    # with self.assertRaises(TypeError) as cm:
    #   op_def_library.apply_op("AttrShape", a=5)
    # self.assertEqual(str(cm.exception),
    #                  "Don't know how to convert 5 to a TensorShapeProto for"
    #                  " argument 'a'")

    with self.assertRaises(TypeError):
        op_def_library.apply_op("AttrShape", a="ABC")
