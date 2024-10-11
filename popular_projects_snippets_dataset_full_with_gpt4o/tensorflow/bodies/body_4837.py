# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# It's very rare to update aggregation=ON_WRITE variables in the forward
# path, and this test case is mainly for completeness.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_WRITE,
            aggregation=tf.VariableAggregation.MEAN)

    @tf.function(input_signature=[])
    def update(self):
        self.v.assign_add(1.)

export_dir = self.get_temp_dir()
with strategy.scope():
    m = Model()
    tf.saved_model.save(m, export_dir)

loaded = tf.saved_model.load(export_dir)
self.assertEqual(self.evaluate(loaded.v), 0.)
loaded.update()
self.assertEqual(self.evaluate(loaded.v), 1.)
