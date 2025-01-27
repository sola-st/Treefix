# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    # Construct a graph with a dynamically shapped input and an internal node
    # that relies on the output of that input's shape.
    in_tensor = array_ops.placeholder(
        shape=[None, None], dtype=dtypes.float32)
    in_tensor2 = [[1, 2], [3, 4]]
    out_tensor = array_ops.reshape(in_tensor2, array_ops.shape(in_tensor))
    sess = session.Session()

converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertAllEqual([1, 1], input_details[0]['shape'])
self.assertAllEqual([-1, -1], input_details[0]['shape_signature'])

# Resize tensor and invoke.
interpreter.resize_tensor_input(0, [4])
interpreter.allocate_tensors()
interpreter.invoke()

# The output should be reshaped properly according to the resized input.
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.int32, output_details[0]['dtype'])
self.assertAllEqual([4], output_details[0]['shape'])
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertAllEqual([1, 2, 3, 4], output_data)
