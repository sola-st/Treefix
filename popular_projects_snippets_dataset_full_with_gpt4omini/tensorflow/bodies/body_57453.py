# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
with ops.Graph().as_default():
    in_tensor = random_ops.random_normal(shape=[1, 16, 16, 3], name='random')
    _ = in_tensor + in_tensor
    sess = session.Session()

# Write graph to file.
graph_def_file = self._getFilepath('model.pb')
write_graph(sess.graph_def, '', graph_def_file, False)
sess.close()

flags_str = ('--graph_def_file={0} --input_arrays={1} '
             '--output_arrays={2}'.format(graph_def_file, 'random', 'add'))
self._run(flags_str, should_succeed=True)
os.remove(graph_def_file)
