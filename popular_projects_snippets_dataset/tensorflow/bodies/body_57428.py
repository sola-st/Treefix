# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name="inputA")
    in_tensor_2 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name="inputB")
    _ = array_ops.fake_quant_with_min_max_args(
        in_tensor_1 + in_tensor_2, min=0., max=1., name="output")
    sess = session.Session()

tflite_model = convert.convert_graphdef_with_arrays(
    sess.graph_def,
    input_arrays_with_shape=[("inputA", [1, 16, 16, 3]),
                             ("inputB", [1, 16, 16, 3])],
    output_arrays=["output"],
    control_output_arrays=None,
    inference_type=dtypes.uint8,
    quantized_input_stats=[(0., 1.), (0., 1.)],
    enable_mlir_converter=False,
)
self.assertTrue(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertEqual(2, len(input_details))
self.assertEqual("inputA", input_details[0]["name"])
self.assertEqual(np.uint8, input_details[0]["dtype"])
self.assertTrue(([1, 16, 16, 3] == input_details[0]["shape"]).all())
self.assertEqual((1., 0.),
                 input_details[0]["quantization"])  # scale, zero_point

self.assertEqual("inputB", input_details[1]["name"])
self.assertEqual(np.uint8, input_details[1]["dtype"])
self.assertTrue(([1, 16, 16, 3] == input_details[1]["shape"]).all())
self.assertEqual((1., 0.),
                 input_details[1]["quantization"])  # scale, zero_point

output_details = interpreter.get_output_details()
self.assertEqual(1, len(output_details))
self.assertEqual("output", output_details[0]["name"])
self.assertEqual(np.uint8, output_details[0]["dtype"])
self.assertTrue(([1, 16, 16, 3] == output_details[0]["shape"]).all())
self.assertGreater(output_details[0]["quantization"][0], 0)  # scale
