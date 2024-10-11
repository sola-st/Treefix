# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[None, 4], dtype=dtypes.float32, name='input1')
    in_tensor_2 = array_ops.placeholder(
        shape=[4, 10], dtype=dtypes.float32, name='input2')
    out_tensor = math_ops.matmul(in_tensor_1, in_tensor_2)
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess,
                                              [in_tensor_1, in_tensor_2],
                                              [out_tensor])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEqual('input1', input_details[0]['name'])
self.assertAllEqual([1, 4], input_details[0]['shape'])
self.assertEqual('input2', input_details[1]['name'])
self.assertAllEqual([4, 10], input_details[1]['shape'])
