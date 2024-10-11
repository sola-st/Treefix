# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
ops.disable_eager_execution()
# Constant folding handles the tf.broadcast_to operation which was not
# supported by the TFLite at the time this test was added.
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(shape=[3], dtype=dtypes.float32)
    y_const = constant_op.constant([1., 2., 3.])
    y_add = y_const + y_const
    out_tensor = in_tensor * y_add
    sess = session.Session()

# Convert model.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor, y_const],
                                              [out_tensor])
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEqual('Placeholder', input_details[0]['name'])
self.assertEqual('Const', input_details[1]['name'])
