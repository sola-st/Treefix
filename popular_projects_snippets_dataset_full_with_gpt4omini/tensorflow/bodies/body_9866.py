# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
x0 = np.array([[1], [2]])
x1 = np.array(range(5))
input_path = os.path.join(test.get_temp_dir(), 'input.npz')
np.savez(input_path, a=x0, b=x1)
input_str = 'x=' + input_path
with self.assertRaises(RuntimeError):
    saved_model_cli.load_inputs_from_input_arg_string(input_str, '', '')
