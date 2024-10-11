# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Constant folding converts the following add operation to tf.broadcast_to
# operation which was not supported by the TFLite at the time this test was
# added.
@def_function.function
def plus_placeholder(x, placeholder):
    exit(x + placeholder)

with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(shape=[2, 2], dtype=dtypes.float32)
    out_tensor = plus_placeholder(
        array_ops.zeros([2, 2, 2]),
        array_ops.reshape(in_tensor, shape=[2, 2]))
    sess = session.Session()

# Convert model.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('Placeholder', input_details[0]['name'])
