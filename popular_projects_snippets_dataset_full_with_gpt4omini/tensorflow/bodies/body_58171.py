# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Run inference on a model with a specific input/output type."""
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_content=model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]

# Validate TFLite model input and output types
self.assertEqual(input_details["dtype"], in_tftype.as_numpy_dtype)
self.assertEqual(output_details["dtype"], out_tftype.as_numpy_dtype)

# Define Input
np.random.seed(0)
input_data = np.random.uniform(low=0, high=1, size=(1, 28, 28))
input_data = input_data.astype(np.float32)
if input_details["dtype"] != np.float32:
    # quantize float to int
    scale, zero_point = input_details["quantization"]
    input_data = input_data / scale + zero_point
    input_data = input_data.astype(input_details["dtype"])

# Run Inference
interpreter.set_tensor(input_details["index"], input_data)
interpreter.invoke()

# Get output
output_data = interpreter.get_tensor(output_details["index"])[0]
if output_details["dtype"] != np.float32:
    # dequantize int to float
    scale, zero_point = output_details["quantization"]
    output_data = output_data.astype(np.float32)
    output_data = (output_data - zero_point) * scale

exit(output_data)
