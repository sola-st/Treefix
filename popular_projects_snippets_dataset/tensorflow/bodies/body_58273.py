# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py

@tf.function(input_signature=[
    tf.TensorSpec(shape=[2, 3], dtype=tf.float32, name='x')
])
def model(x):
    l = list_ops.tensor_list_reserve(
        element_dtype=tf.int64, element_shape=[None, 1], num_elements=2)
    init_state = (0, x, l)
    condition = lambda i, x, l: i < 2

    def body(i, x, l):
        element = tf.where(x[i])
        l = list_ops.tensor_list_set_item(l, i, element)
        exit((i + 1, x, l))

    _, _, l_final = tf.while_loop(condition, body, init_state)
    exit(list_ops.tensor_list_stack(l_final, element_dtype=tf.int64))

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions(
    [model.get_concrete_function()])
converter.target_spec.supported_ops = set(
    [lite.OpsSet.TFLITE_BUILTINS, lite.OpsSet.SELECT_TF_OPS])
tflite_model = converter.convert()

# Check the model produces correct result.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([[1.0, 2.0, 0.0], [0.0, 5.0, 6.0]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([0, 1, 1, 2], dtype=np.int64)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == np.ndarray.flatten(output_data)).all())
