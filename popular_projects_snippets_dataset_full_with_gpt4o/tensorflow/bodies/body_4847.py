# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# Reading a synchronizaiton=ON_READ in the replica context should just read
# the local value. Reading it in the cross replica context aggregates the
# value from all replicas. Both are true with a loaded model.
#
# Note that if aggregation=SUM, the value of each replica is the saved value
# divided by the number of replicas. In this way if you load a model and
# save it again, the values of the variables don't change.

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
value = strategy.experimental_distribute_values_from_function(
    lambda ctx: tf.identity([3., 7.][ctx.replica_id_in_sync_group]))
with strategy.scope():
    m = Model()
    strategy.run(m.v.assign, args=(value,))
    self.assertAllEqual(
        self.evaluate(strategy.experimental_local_results(m.v)), [3., 7.])
    self.assertEqual(self.evaluate(m.v.read_value()), 10.)
    tf.saved_model.save(m, export_dir)
    del m

with strategy.scope():
    loaded = tf.saved_model.load(export_dir)
# It's intended that we don't save the each replica, but just the aggregated
# value.
self.assertAllEqual(
    self.evaluate(
        strategy.experimental_local_results(strategy.run(loaded))),
    [5., 5.])
self.assertEqual(self.evaluate(loaded.v.read_value()), 10.)

# save and load again.
export_dir2 = self.get_temp_dir()
tf.saved_model.save(loaded, export_dir2)
# loaded.v.read_value() is still 1., both with and without strategy.
loaded = tf.saved_model.load(export_dir2)
self.assertEqual(self.evaluate(loaded.v.read_value()), 10.)
with strategy.scope():
    loaded = tf.saved_model.load(export_dir2)
    self.assertEqual(self.evaluate(loaded.v.read_value()), 10.)
