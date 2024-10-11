# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("TypeList", a=["foo"], name="z")
    self.assertProtoEquals("""
        name: 'z' op: 'TypeList' input: 'z/a_0'
        attr { key: 'T' value { list { type: DT_STRING } } }
        """, op.node_def)

    op = op_def_library.apply_op("TypeList", a=[True, 12], name="y")
    self.assertProtoEquals("""
        name: 'y' op: 'TypeList' input: 'y/a_0' input: 'y/a_1'
        attr { key: 'T' value { list { type: DT_BOOL type: DT_INT32 } } }
        """, op.node_def)

    op = op_def_library.apply_op("TypeList", a=[], name="empty")
    self.assertProtoEquals("""
        name: 'empty' op: 'TypeList' attr { key: 'T' value { list { } } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("TypeList", a=17)
    self.assertStartsWith(str(cm.exception),
                          "Expected list for 'a' "
                          "argument to 'TypeList' Op, not ")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("TypeList", a=[self.Tensor(dtypes.int32), None])
    self.assertStartsWith(str(cm.exception),
                          "Tensors in list passed to 'a' of 'TypeList' Op "
                          "have types [int32, <NOT CONVERTIBLE TO TENSOR>]")
