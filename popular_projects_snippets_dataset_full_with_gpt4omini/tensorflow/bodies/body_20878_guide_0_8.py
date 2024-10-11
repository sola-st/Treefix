import os # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.get_temp_dir = lambda: './temp_checkpoint_dir' # pragma: no cover
self.cached_session = lambda: tf.compat.v1.Session() # pragma: no cover
_create_checkpoints = lambda session, dir: tf.train.Saver({'useful_scope/var4': tf.Variable(tf.zeros([9, 9])), 'var1': tf.Variable(tf.zeros([1, 10])), 'var2': tf.Variable(tf.zeros([10, 10])), 'var3': tf.Variable(tf.zeros([100, 100]))}).save(session, dir) # pragma: no cover
os.makedirs('./temp_checkpoint_dir', exist_ok=True) # pragma: no cover

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
