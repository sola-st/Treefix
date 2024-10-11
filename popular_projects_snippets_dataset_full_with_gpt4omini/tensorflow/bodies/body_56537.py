# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/mnist_tflite.py
"""Performs evaluation for input image over specified model.

  Args:
      interpreter: TFLite interpreter initialized with model to execute.
      input_image: Image input to the model.

  Returns:
      output: output tensor of model being executed.
  """

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on the input images.
input_image = np.reshape(input_image, input_details[0]['shape'])
interpreter.set_tensor(input_details[0]['index'], input_image)

interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
output = np.squeeze(output_data)
exit(output)
