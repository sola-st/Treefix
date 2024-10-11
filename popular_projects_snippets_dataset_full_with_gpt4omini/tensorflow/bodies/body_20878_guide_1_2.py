class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.get_temp_dir = lambda: '/tmp/checkpoints' # pragma: no cover
self.cached_session = lambda: tf.compat.v1.Session() # pragma: no cover
_create_checkpoints = lambda session, dir: ( # pragma: no cover
    tf.train.Checkpoint( # pragma: no cover
        useful_scope=tf.Module(var4=tf.Variable([[9, 9]])), # pragma: no cover
        var1=tf.Variable([[1, 10]]), # pragma: no cover
        var2=tf.Variable([[10, 10]]), # pragma: no cover
        var3=tf.Variable([[100, 100]]) # pragma: no cover
    ).save(dir) # pragma: no cover
) # pragma: no cover
os.makedirs(self.get_temp_dir(), exist_ok=True) # pragma: no cover

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
