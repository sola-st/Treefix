# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/python/modify_model_interface_lib_test.py
# 1. SETUP
# Define the temporary directory and files
temp_dir = self.get_temp_dir()
initial_file = os.path.join(temp_dir, 'initial_model.tflite')
final_file = os.path.join(temp_dir, 'final_model.tflite')
# Define initial model
initial_model = build_tflite_model_with_full_integer_quantization(
    supported_ops=tf.lite.OpsSet
    .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8)
with open(initial_file, 'wb') as model_file:
    model_file.write(initial_model)

# 2. INVOKE
# Invoke the modify_model_interface function
modify_model_interface_lib.modify_model_interface(initial_file, final_file,
                                                  tf.int16, tf.int16)

# 3. VALIDATE
# Load TFLite model and allocate tensors.
initial_interpreter = tf.lite.Interpreter(model_path=initial_file)
initial_interpreter.allocate_tensors()
final_interpreter = tf.lite.Interpreter(model_path=final_file)
final_interpreter.allocate_tensors()

# Get input and output types.
initial_input_dtype = initial_interpreter.get_input_details()[0]['dtype']
initial_output_dtype = initial_interpreter.get_output_details()[0]['dtype']
final_input_dtype = final_interpreter.get_input_details()[0]['dtype']
final_output_dtype = final_interpreter.get_output_details()[0]['dtype']

# Validate the model interfaces
self.assertEqual(initial_input_dtype, np.float32)
self.assertEqual(initial_output_dtype, np.float32)
self.assertEqual(final_input_dtype, np.int16)
self.assertEqual(final_output_dtype, np.int16)
