# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
from l3.Runtime import _l_
x0 = np.array([[1], [2]])
_l_(20476)
input_path = os.path.join(test.get_temp_dir(), 'input.npz')
_l_(20477)
np.savez(input_path, a=x0)
_l_(20478)
input_str = 'x=' + input_path + '[a];y=' + input_path
_l_(20479)
feed_dict = saved_model_cli.load_inputs_from_input_arg_string(
    input_str, '', '')
_l_(20480)
self.assertTrue(np.all(feed_dict['x'] == x0))
_l_(20481)
self.assertTrue(np.all(feed_dict['y'] == x0))
_l_(20482)
