# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Tests converting a graph with an op that have multiple outputs."""
with ops.Graph().as_default():
    input_tensor = array_ops.placeholder(shape=[4], dtype=dtypes.float32)
    out0, out1, out2, out3 = array_ops.split(
        input_tensor, [1, 1, 1, 1], axis=0)
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [input_tensor],
                                              [out0, out1, out2, out3])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
interpreter.set_tensor(input_details[0]['index'],
                       np.asarray([1.0, 2.0, 3.0, 4.0], dtype=np.float32))
interpreter.invoke()

output_details = interpreter.get_output_details()
self.assertLen(output_details, 4)
self.assertEqual(1.0, interpreter.get_tensor(output_details[0]['index']))
self.assertEqual(2.0, interpreter.get_tensor(output_details[1]['index']))
self.assertEqual(3.0, interpreter.get_tensor(output_details[2]['index']))
self.assertEqual(4.0, interpreter.get_tensor(output_details[3]['index']))
