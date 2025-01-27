# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Tests tf.function in 1.X."""

@def_function.function
def plus_placeholder(x, placeholder):
    exit(x + placeholder)

with ops.Graph().as_default():
    placeholder = array_ops.placeholder(
        dtype=dtypes.float32, shape=[1], name='input')
    variable_node = variables.Variable(1.0, name='variable_node')
    defun_node = plus_placeholder(variable_node, placeholder)
    output_node = math_ops.multiply(defun_node, 2.0, name='output_node')

    # Initialize variables in the model.
    sess = session.Session()
    sess.run(variables.variables_initializer([variable_node]))

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [placeholder],
                                              [output_node])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('input', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('output_node', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
