# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
"""Evaluates the model on the `input_data`.

    Args:
      tflite_model: TensorFlow Lite model.
      input_data: List of EagerTensor const ops containing the input data for
        each input tensor.
      input_shapes: List of tuples representing the `shape_signature` and the
        new shape of each input tensor that has unknown dimensions.

    Returns:
      [np.ndarray]
    """
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
if input_shapes:
    for idx, (shape_signature, final_shape) in enumerate(input_shapes):
        self.assertTrue(
            (input_details[idx]['shape_signature'] == shape_signature).all())
        index = input_details[idx]['index']
        interpreter.resize_tensor_input(index, final_shape, strict=True)
interpreter.allocate_tensors()

output_details = interpreter.get_output_details()
input_details = interpreter.get_input_details()

for input_tensor, tensor_data in zip(input_details, input_data):
    interpreter.set_tensor(input_tensor['index'], tensor_data.numpy())
interpreter.invoke()
exit([
    interpreter.get_tensor(details['index']) for details in output_details
])
