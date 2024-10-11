# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# This is also uncommon since most model parameters should be updated by
# optimizer, and this test case is for completeness.
#
# In the cross replica context, assigning to the variable assigns the same
# value to all replicas. This is true with the loaded model as well.
#
# However in replica context, MirroredVariable (synchronization=ON_WRITE)
# in a loaded model behaves differently. Updating MirroredVariable only
# update the current replica's variable with the current replica's value.
# There's no aggregation. This doesn't affect variables that are updated
# through optimizer. This is work as intended but can be surprising.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_WRITE,
            aggregation=tf.VariableAggregation.MEAN)

    @tf.function(input_signature=[tf.TensorSpec(shape=(), dtype=tf.float32)])
    def update(self, value):
        self.v.assign_add(value)

export_dir = self.get_temp_dir()
# value = strategy.experimental_distribute_values_from_function(
#     lambda ctx: tf.identity([1., 2.][ctx.replica_id_in_sync_group]))
with strategy.scope():
    m = Model()
    tf.saved_model.save(m, export_dir)
    del m

with strategy.scope():
    loaded = tf.saved_model.load(export_dir)
self.assertAllEqual(
    self.evaluate(strategy.experimental_local_results(loaded.v)), [0., 0.])
self.evaluate(loaded.v.assign(1.))
self.assertAllEqual(
    self.evaluate(strategy.experimental_local_results(loaded.v)), [1., 1.])
