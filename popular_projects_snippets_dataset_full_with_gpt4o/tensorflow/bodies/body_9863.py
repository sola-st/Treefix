# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
x0 = np.array([[1], [2]])
x1 = np.array(range(6)).reshape(2, 3)
input0_path = os.path.join(test.get_temp_dir(), 'input0.npy')
input1_path = os.path.join(test.get_temp_dir(), 'input1.npy')
np.save(input0_path, x0)
np.save(input1_path, x1)
input_str = 'x0=' + input0_path + '[x0];x1=' + input1_path
feed_dict = saved_model_cli.load_inputs_from_input_arg_string(
    input_str, '', '')
self.assertTrue(np.all(feed_dict['x0'] == x0))
self.assertTrue(np.all(feed_dict['x1'] == x1))
