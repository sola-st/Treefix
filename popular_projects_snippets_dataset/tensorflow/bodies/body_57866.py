# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# SETUP
# 1. Define input shapes
tf_input_shape = (32, 32, 128)
tflite_input_shape = (1,) + tf_input_shape
# 2. Define model
tf_saved_model_dir, input_name, output_name = (
    self._createV2QATSavedModel(tf_input_shape))

# MODEL 1: TFLite (float) model
# 1. Create TFLite model
converter = tf.lite.TFLiteConverter.from_saved_model(tf_saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
# 2. Initialize the Intepreter
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
interpreter.resize_tensor_input(input_details['index'], tflite_input_shape)
interpreter.allocate_tensors()
signature_list = interpreter._get_full_signature_list()['serving_default']
# 3. (Skip) Verify that signature def input/output tensors are in the model.
# 4. Evaluate the model
input_data = np.random.random(tflite_input_shape).astype(np.float32)
result = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model, 'serving_default', {input_name: input_data})[output_name]

# MODEL 2: TFLite (full integer quantized) model
# 1. Create TFLite model
converter = tf.lite.TFLiteConverter.from_saved_model(tf_saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
tflite_model_quant = converter.convert()
# 2. Initialize the Intepreter
interpreter = Interpreter(model_content=tflite_model_quant)
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
interpreter.resize_tensor_input(input_details['index'], tflite_input_shape)
interpreter.allocate_tensors()
# 3. Verify that signature def input/output tensors are in the model.
all_indices = {item['index'] for item in interpreter.get_tensor_details()}
signature_list = interpreter._get_full_signature_list()['serving_default']
input_tensor_indices = set(signature_list['inputs'].values())
assert input_tensor_indices.issubset(all_indices)
output_tensor_indices = set(signature_list['outputs'].values())
assert output_tensor_indices.issubset(all_indices)

# 4. Evaluate the model
input_data = np.random.random(tflite_input_shape)
input_scale, input_zero_point = input_details['quantization']
if (input_scale, input_zero_point) != (0.0, 0):
    input_data = input_data / input_scale + input_zero_point
    input_data = input_data.astype(input_details['dtype'])
result_quant = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model_quant, 'serving_default',
    {input_name: input_data})[output_name]
output_scale, output_zero_point = output_details['quantization']
if (output_scale, output_zero_point) != (0.0, 0):
    result_quant = result_quant.astype(np.float32)
    result_quant = (result_quant - output_zero_point) * output_scale

# COMPARE: Validate that results from both models are approx. the same.
root_mean_squared = np.sqrt(np.mean((result-result_quant)**2))
assert root_mean_squared < 1.0
