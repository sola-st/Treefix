class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
def _create_checkpoints(session, checkpoint_dir): pass# pragma: no cover
_create_checkpoints = _create_checkpoints # pragma: no cover
checkpoint_utils = type('MockCheckpointUtils', (object,), {'list_variables': lambda x: []})() # pragma: no cover

class Mock:# pragma: no cover
    def get_temp_dir(self): return '/tmp/checkpoint_dir'# pragma: no cover
    def cached_session(self): return tf.compat.v1.Session()# pragma: no cover
    def assertEqual(self, a, b): assert a == b# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
_create_checkpoints = lambda session, checkpoint_dir: None # pragma: no cover
checkpoint_utils = type('MockCheckpointUtils', (object,), {'list_variables': lambda checkpoint_dir: [('useful_scope/var4', [9, 9]), ('var1', [1, 10]), ('var2', [10, 10]), ('var3', [100, 100])]})() # pragma: no cover

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
