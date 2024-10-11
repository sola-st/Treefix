import os # pragma: no cover

dirname = 'test_directory' # pragma: no cover
self = type('MockSelf', (object,), {'get_temp_dir': lambda self: '/tmp'})() # pragma: no cover
gfile = type('MockGFile', (object,), {'MakeDirs': lambda self, path: None})() # pragma: no cover

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
