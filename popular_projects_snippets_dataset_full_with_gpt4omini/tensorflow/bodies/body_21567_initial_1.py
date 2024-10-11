import os # pragma: no cover
import tempfile # pragma: no cover
from unittest import mock # pragma: no cover

self = mock.Mock() # pragma: no cover
self.get_temp_dir = mock.Mock(return_value=tempfile.mkdtemp()) # pragma: no cover
dirname = 'test_directory' # pragma: no cover
gfile = mock.Mock() # pragma: no cover
gfile.MakeDirs = mock.Mock() # pragma: no cover

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
