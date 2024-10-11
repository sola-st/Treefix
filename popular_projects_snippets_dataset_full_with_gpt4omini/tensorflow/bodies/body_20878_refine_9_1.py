class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
def _create_checkpoints(session, directory):# pragma: no cover
    tfv1.create_file_writer(directory).write('Checkpoints created.')# pragma: no cover
_create_checkpoints = _create_checkpoints # pragma: no cover
checkpoint_utils = type('MockCheckpointUtils', (), {'list_variables': staticmethod(lambda dir: [('useful_scope/var4', [9, 9]), ('var1', [1, 10]), ('var2', [10, 10]), ('var3', [100, 100])])})() # pragma: no cover
def get_temp_dir(self): return '/tmp/checkpoints'# pragma: no cover
self.get_temp_dir = get_temp_dir # pragma: no cover
def cached_session(self): return tfv1.Session()# pragma: no cover
self.cached_session = cached_session # pragma: no cover
def assertEqual(self, a, b): assert a == b, f'Assertion failed: {a} != {b}'# pragma: no cover
self.assertEqual = assertEqual # pragma: no cover

import os # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.get_temp_dir = lambda: '/tmp/checkpoints' # pragma: no cover
self.cached_session = lambda: tf.compat.v1.Session() # pragma: no cover
self.assertEqual = lambda a, b: a == b # pragma: no cover
_create_checkpoints = lambda session, dir: None # pragma: no cover
checkpoint_utils = type('MockCheckpointUtils', (object,), {'list_variables': staticmethod(lambda dir: [('useful_scope/var4', [9, 9]), ('var1', [1, 10]), ('var2', [10, 10]), ('var3', [100, 100])])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
from l3.Runtime import _l_
checkpoint_dir = self.get_temp_dir()
_l_(8642)
with self.cached_session() as session:
    _l_(8644)

    _create_checkpoints(session, checkpoint_dir)
    _l_(8643)
self.assertEqual(
    checkpoint_utils.list_variables(checkpoint_dir),
    [("useful_scope/var4", [9, 9]), ("var1", [1, 10]), ("var2", [10, 10]),
     ("var3", [100, 100])])
_l_(8645)
