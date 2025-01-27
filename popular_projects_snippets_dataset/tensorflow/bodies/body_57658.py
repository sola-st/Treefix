# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a shape overriding case."""
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32)
    _ = in_tensor + in_tensor
    sess = session.Session()

# Write graph to file.
graph_def_file = os.path.join(self.get_temp_dir(), 'model.pb')
write_graph(sess.graph_def, '', graph_def_file, False)
sess.close()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_frozen_graph(
    graph_def_file, ['Placeholder'], ['add'],
    input_shapes={'Placeholder': [2, 16, 16, 3]})
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertAllEqual([2, 16, 16, 3], input_details[0]['shape'])
