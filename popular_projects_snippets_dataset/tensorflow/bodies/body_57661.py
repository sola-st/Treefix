# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    var = variable_scope.get_variable(
        'weights', shape=[1, 16, 16, 3], dtype=dtypes.float32)
    _ = in_tensor + var
    sess = session.Session()

# Write graph to file.
graph_def_file = os.path.join(self.get_temp_dir(), 'model.pb')
write_graph(sess.graph_def, '', graph_def_file, False)
sess.close()

# Ensure the graph with variables cannot be converted.
with self.assertRaises(ValueError) as error:
    lite.TFLiteConverter.from_frozen_graph(graph_def_file, ['Placeholder'],
                                           ['add'])
self.assertEqual('Please freeze the graph using freeze_graph.py.',
                 str(error.exception))
