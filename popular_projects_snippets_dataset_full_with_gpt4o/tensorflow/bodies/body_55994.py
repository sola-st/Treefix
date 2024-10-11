# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
x = constant_op.constant(32, dtype=dtypes.float32)
y = constant_op.constant(32, dtype=dtypes.float32)

attrs, inputs, input_types, output_structure = (
    op_def_library_pybind.process_inputs("AddV2", 1, {
        "x": x,
        "y": y
    }))

proto = text_format.Parse("type: DT_FLOAT", attr_value_pb2.AttrValue())
self.assertEqual(attrs, {"T": proto})
self.assertEqual(inputs, [x, y])
self.assertEqual(input_types, [dtypes.float32, dtypes.float32])
self.assertEqual(output_structure, [None])
