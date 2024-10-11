# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Modify the float input/output type of an integer quantized model."""

def _run_tflite_inference(model, in_tftype, out_tftype):
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

if is_post_train and quantization_type == tf.int8:
    model = self.__class__.post_train_int8_model
elif is_post_train and quantization_type == tf.int16:
    model = self.__class__.post_train_int16_model
else:
    model = None
# Run model inference with float input output type
output_data = _run_tflite_inference(model, tf.float32, tf.float32)
# Modify the model io types to the target input/output types.
model_io = util.modify_model_io_type(model, in_tftype, out_tftype)
# Run model inference with modified integer input output type
output_io_data = _run_tflite_inference(model_io, in_tftype, out_tftype)
# Validate that both the outputs are the same
self.assertAllClose(output_data, output_io_data, atol=1.0)

# Modify the model with the target input/output types should be a no op.
model_io = util.modify_model_io_type(model_io, in_tftype, out_tftype)
# Run model inference with modified integer input output type
output_io_data = _run_tflite_inference(model_io, in_tftype, out_tftype)
# Validate that both the outputs are the same
self.assertAllClose(output_data, output_io_data, atol=1.0)
