import os # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (), {'get_temp_dir': lambda: 'temp_dir'})() # pragma: no cover
dirname = 'test_directory' # pragma: no cover
gfile = type('Mock', (), {'MakeDirs': lambda x: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
from l3.Runtime import _l_
test_dir = os.path.join(self.get_temp_dir(), dirname)
_l_(8184)
gfile.MakeDirs(test_dir)
_l_(8185)
aux = test_dir
_l_(8186)
exit(aux)
