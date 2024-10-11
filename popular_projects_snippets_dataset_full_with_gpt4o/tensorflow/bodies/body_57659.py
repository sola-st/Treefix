# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test an invalid shape overriding case, which has a wrong input name."""
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
with self.assertRaises(ValueError):
    lite.TFLiteConverter.from_frozen_graph(
        graph_def_file, ['Placeholder'], ['add'],
        input_shapes={'wrong_input': [2, 16, 16, 3]})
