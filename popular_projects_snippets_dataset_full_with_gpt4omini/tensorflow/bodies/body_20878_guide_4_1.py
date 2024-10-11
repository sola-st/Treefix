import os # pragma: no cover

class MockSelf: # pragma: no cover
    def get_temp_dir(self): # pragma: no cover
        return './tmp_checkpoints' # pragma: no cover
    def cached_session(self): # pragma: no cover
        return tf.compat.v1.Session() # pragma: no cover
self = MockSelf() # pragma: no cover
checkpoint_dir = self.get_temp_dir() # pragma: no cover
os.makedirs(checkpoint_dir, exist_ok=True) # pragma: no cover
def _create_checkpoints(session, checkpoint_dir): # pragma: no cover
    var1 = tf.Variable([1, 10], name='var1') # pragma: no cover
    var2 = tf.Variable([10, 10], name='var2') # pragma: no cover
    var3 = tf.Variable([100, 100], name='var3') # pragma: no cover
    var4 = tf.Variable([[9, 9]], name='useful_scope/var4') # pragma: no cover
    tf.global_variables_initializer().run(session=session) # pragma: no cover
    tf.train.Saver({'var1': var1, 'var2': var2, 'var3': var3, 'useful_scope/var4': var4}).save(session, checkpoint_dir + '/model.ckpt') # pragma: no cover

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
