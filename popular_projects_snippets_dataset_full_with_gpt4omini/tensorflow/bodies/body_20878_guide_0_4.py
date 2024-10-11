self = type('Mock', (object,), {})() # pragma: no cover
self.get_temp_dir = lambda: '/tmp/checkpoints' # pragma: no cover
self.cached_session = lambda: tf.Session() # pragma: no cover
def _create_checkpoints(session, directory): # pragma: no cover
    # Simulate checkpoints creation # pragma: no cover
    var4 = tf.Variable(tf.ones([9, 9]), name='useful_scope/var4') # pragma: no cover
    var1 = tf.Variable(tf.ones([1, 10])*1, name='var1') # pragma: no cover
    var2 = tf.Variable(tf.ones([10, 10])*10, name='var2') # pragma: no cover
    var3 = tf.Variable(tf.ones([100, 100])*100, name='var3') # pragma: no cover
    tf.global_variables_initializer().run(session=session) # pragma: no cover
    tf.train.Saver().save(session, directory + '/model.ckpt') # pragma: no cover

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
