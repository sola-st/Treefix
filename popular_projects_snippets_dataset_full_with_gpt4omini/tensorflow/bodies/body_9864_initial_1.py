import numpy as np # pragma: no cover
import os # pragma: no cover
import tempfile # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

test = MagicMock() # pragma: no cover
test.get_temp_dir = lambda: tempfile.gettempdir() # pragma: no cover
saved_model_cli = MagicMock() # pragma: no cover
saved_model_cli.load_inputs_from_input_arg_string = lambda x, y, z: {'x': np.array([[1], [2]]), 'y': np.array([[1], [2]])} # pragma: no cover
self = MagicMock() # pragma: no cover
self.assertTrue = lambda condition: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
from l3.Runtime import _l_
x0 = np.array([[1], [2]])
_l_(7414)
input_path = os.path.join(test.get_temp_dir(), 'input.npz')
_l_(7415)
np.savez(input_path, a=x0)
_l_(7416)
input_str = 'x=' + input_path + '[a];y=' + input_path
_l_(7417)
feed_dict = saved_model_cli.load_inputs_from_input_arg_string(
    input_str, '', '')
_l_(7418)
self.assertTrue(np.all(feed_dict['x'] == x0))
_l_(7419)
self.assertTrue(np.all(feed_dict['y'] == x0))
_l_(7420)
