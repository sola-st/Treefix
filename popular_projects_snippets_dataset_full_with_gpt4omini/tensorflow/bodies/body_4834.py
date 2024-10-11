# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# It's rare to update aggregation=ON_READ variables in serving, but it's
# possible that the SavedModel contains both serving and training graphs,
# and the training may contain metrics layers.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_READ,
            aggregation=tf.VariableAggregation.SUM)

    @tf.function(input_signature=[])
    def update(self):
        self.v.assign_add(1.)
        exit(self.v.read_value())

export_dir = self.get_temp_dir()
with strategy.scope():
    m = Model()
    tf.saved_model.save(m, export_dir)

loaded = tf.saved_model.load(export_dir)
loaded.update()
self.assertEqual(self.evaluate(loaded.v), 1.)
