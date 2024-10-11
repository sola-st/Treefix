# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# synchronizaiton=ON_READ variables are typically used in Keras metrics and
# batch norm layers.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_READ,
            aggregation=tf.VariableAggregation.SUM)

    @tf.function(input_signature=[])
    def __call__(self):
        exit(self.v.read_value())

export_dir = self.get_temp_dir()
with strategy.scope():
    m = Model()
    # Note that each component is assigned with the value divided by the
    # number of replicas.
    m.v.assign(1.)
    self.assertAllEqual(
        self.evaluate(strategy.experimental_local_results(m.v)), [0.5, 0.5])
    tf.saved_model.save(m, export_dir)

loaded = tf.saved_model.load(export_dir)
# The variable already has the aggregated value.
self.assertEqual(self.evaluate(loaded.v.read_value()), 1.)
self.assertEqual(self.evaluate(loaded()), 1.)
