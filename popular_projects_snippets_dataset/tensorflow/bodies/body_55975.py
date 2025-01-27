# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("NPolymorphicIn", a=[1, 2], name="n")
    self.assertProtoEquals("""
        name: 'n' op: 'NPolymorphicIn' input: 'n/a_0' input: 'n/a_1'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NPolymorphicIn", a=[5, 4, 3, 2, 1], name="o")
    self.assertProtoEquals("""
        name: 'o' op: 'NPolymorphicIn'
        input: 'o/a_0' input: 'o/a_1' input: 'o/a_2' input: 'o/a_3' input: 'o/a_4'
        attr { key: 'T' value { type: DT_INT32 } }
        attr { key: 'N' value { i: 5 } }
        """, op.node_def)

    op = op_def_library.apply_op("NPolymorphicIn", a=["foo", "bar"], name="p")
    self.assertProtoEquals("""
        name: 'p' op: 'NPolymorphicIn' input: 'p/a_0' input: 'p/a_1'
        attr { key: 'T' value { type: DT_STRING } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NPolymorphicIn",
        a=[1, self.Tensor(dtypes.float32, name="x")],
        name="q")
    self.assertProtoEquals("""
        name: 'q' op: 'NPolymorphicIn' input: 'q/a_0' input: 'x'
        attr { key: 'T' value { type: DT_FLOAT } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    op = op_def_library.apply_op(
        "NPolymorphicIn",
        a=[
            self.Tensor(dtypes.float32, name="y"),
            self.Tensor(dtypes.float32_ref, name="z")
        ],
        name="r")
    self.assertProtoEquals("""
        name: 'r' op: 'NPolymorphicIn' input: 'y' input: 'z'
        attr { key: 'T' value { type: DT_FLOAT } }
        attr { key: 'N' value { i: 2 } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("NPolymorphicIn", a=[99])
    self.assertEqual(str(cm.exception),
                     "List argument 'a' to 'NPolymorphicIn' Op with length 1 "
                     "shorter than minimum length 2.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicIn", a=[38, "bar"])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NPolymorphicIn' Op "
                     "have types [int32, string] that don't all match.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NPolymorphicIn", a=[38, self.Tensor(dtypes.string)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NPolymorphicIn' Op "
                     "have types [int32, string] that don't all match.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicIn", a=[38, None])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NPolymorphicIn' Op "
                     "have types [int32, <NOT CONVERTIBLE TO TENSOR>] that "
                     "don't all match.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "NPolymorphicIn", a=["abcd", self.Tensor(dtypes.int32)])
    self.assertEqual(str(cm.exception),
                     "Tensors in list passed to 'a' of 'NPolymorphicIn' Op "
                     "have types [string, int32] that don't all match.")

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("NPolymorphicIn", a=17)
    self.assertStartsWith(str(cm.exception),
                          "Expected list for 'a' argument "
                          "to 'NPolymorphicIn' Op, not ")
