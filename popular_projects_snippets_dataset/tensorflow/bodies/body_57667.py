# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    _ = in_tensor + in_tensor
    sess = session.Session()

# Write graph to file.
graph_def_file = os.path.join(self.get_temp_dir(), 'model.pb')
write_graph(sess.graph_def, '', graph_def_file, False)
sess.close()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_frozen_graph(graph_def_file,
                                                   ['Placeholder'], ['add'])
converter.exclude_conversion_metadata = True
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNone(metadata)
