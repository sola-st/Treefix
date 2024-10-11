# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
input_data = constant_op.constant(1., shape=[1])
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(3.)
root.v2 = variables.Variable(2.)
root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter.target_spec.supported_ops = set([lite.OpsSet.SELECT_TF_OPS])
converter.experimental_new_converter = enable_mlir
tflite_model = converter.convert()

# Check the model works with TensorFlow ops.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([4.0], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([24.0], dtype=np.float32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
