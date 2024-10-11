# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputA')
    in_tensor_2 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputB')
    _ = array_ops.fake_quant_with_min_max_args(
        in_tensor_1 + in_tensor_2, min=0., max=1., name='output',
        num_bits=16)  # INT8 inference type works for 16 bits fake quant.
    sess = session.Session()

# Write graph to file.
graph_def_file = self._getFilepath('model.pb')
write_graph(sess.graph_def, '', graph_def_file, False)
sess.close()

flags_str = ('--inference_type=INT8 --std_dev_values=128,128 '
             '--mean_values=128,128 '
             '--graph_def_file={0} --input_arrays={1},{2} '
             '--output_arrays={3}'.format(graph_def_file, 'inputA',
                                          'inputB', 'output'))
self._run(flags_str, should_succeed=True)
os.remove(graph_def_file)
