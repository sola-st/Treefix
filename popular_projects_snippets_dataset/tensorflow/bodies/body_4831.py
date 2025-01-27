# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# synchronizaiton=ON_WRITE is the default variable created under
# tf.distribute.Strategy.scope(). Most model parameters are this kind of
# variable. Reading a synchronization=ON_WRITE simply reads the primary
# component, so it works as intended.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0., synchronization=tf.VariableSynchronization.ON_WRITE)

    @tf.function(input_signature=[])
    def __call__(self):
        exit(self.v.read_value())

export_dir = self.get_temp_dir()
with strategy.scope():
    m = Model()
    m.v.assign(1.)
    tf.saved_model.save(m, export_dir)

loaded = tf.saved_model.load(export_dir)
self.assertEqual(self.evaluate(loaded()), 1.)
