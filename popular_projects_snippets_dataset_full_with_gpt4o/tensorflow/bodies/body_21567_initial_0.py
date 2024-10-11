import os # pragma: no cover
import tempfile # pragma: no cover

self = type('Mock', (object,), {'get_temp_dir': lambda self: tempfile.gettempdir()})() # pragma: no cover
dirname = 'my_test_directory' # pragma: no cover
gfile = type('Mock', (object,), {'MakeDirs': lambda path: os.makedirs(path, exist_ok=True)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
from l3.Runtime import _l_
test_dir = os.path.join(self.get_temp_dir(), dirname)
_l_(21312)
gfile.MakeDirs(test_dir)
_l_(21313)
aux = test_dir
_l_(21314)
exit(aux)
