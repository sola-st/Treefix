import os # pragma: no cover
from unittest import mock # pragma: no cover

self = type('Mock', (object,), {'get_temp_dir': lambda self: os.path.join('/tmp', 'checkpoint'), 'cached_session': lambda self: mock.MagicMock(), 'assertEqual': lambda self, a, b: a == b})() # pragma: no cover
_create_checkpoints = lambda session, checkpoint_dir: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
from l3.Runtime import _l_
checkpoint_dir = self.get_temp_dir()
_l_(21427)
with self.cached_session() as session:
    _l_(21429)

    _create_checkpoints(session, checkpoint_dir)
    _l_(21428)
self.assertEqual(
    checkpoint_utils.list_variables(checkpoint_dir),
    [("useful_scope/var4", [9, 9]), ("var1", [1, 10]), ("var2", [10, 10]),
     ("var3", [100, 100])])
_l_(21430)
