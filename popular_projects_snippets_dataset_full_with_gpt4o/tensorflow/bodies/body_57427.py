# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name="input")
    _ = in_tensor + in_tensor
    sess = session.Session()

tflite_model = convert.convert_graphdef_with_arrays(
    sess.graph_def,
    input_arrays_with_shape=[("input", [1, 16, 16, 3])],
    output_arrays=["add"],
    control_output_arrays=None,
    inference_type=dtypes.float32,
    enable_mlir_converter=False)
self.assertTrue(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertEqual(1, len(input_details))
self.assertEqual("input", input_details[0]["name"])
self.assertEqual(np.float32, input_details[0]["dtype"])
self.assertTrue(([1, 16, 16, 3] == input_details[0]["shape"]).all())
self.assertEqual((0., 0.), input_details[0]["quantization"])

output_details = interpreter.get_output_details()
self.assertEqual(1, len(output_details))
self.assertEqual("add", output_details[0]["name"])
self.assertEqual(np.float32, output_details[0]["dtype"])
self.assertTrue(([1, 16, 16, 3] == output_details[0]["shape"]).all())
self.assertEqual((0., 0.), output_details[0]["quantization"])
