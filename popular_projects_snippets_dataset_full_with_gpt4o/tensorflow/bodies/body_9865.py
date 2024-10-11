# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
pkl0 = {'a': 5, 'b': np.array(range(4))}
pkl1 = np.array([1])
pkl2 = np.array([[1], [3]])
input_path0 = os.path.join(test.get_temp_dir(), 'pickle0.pkl')
input_path1 = os.path.join(test.get_temp_dir(), 'pickle1.pkl')
input_path2 = os.path.join(test.get_temp_dir(), 'pickle2.pkl')
with open(input_path0, 'wb') as f:
    pickle.dump(pkl0, f)
with open(input_path1, 'wb') as f:
    pickle.dump(pkl1, f)
with open(input_path2, 'wb') as f:
    pickle.dump(pkl2, f)
input_str = 'x=' + input_path0 + '[b];y=' + input_path1 + '[c];'
input_str += 'z=' + input_path2
feed_dict = saved_model_cli.load_inputs_from_input_arg_string(
    input_str, '', '')
self.assertTrue(np.all(feed_dict['x'] == pkl0['b']))
self.assertTrue(np.all(feed_dict['y'] == pkl1))
self.assertTrue(np.all(feed_dict['z'] == pkl2))
