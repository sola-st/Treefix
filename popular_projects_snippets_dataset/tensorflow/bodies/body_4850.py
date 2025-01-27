# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# Updating a synchronizaiton=ON_READ in the replica context should just
# update the local value. Updating it in the cross replica context updates
# each component of the variable. Both are true with a loaded model.
#
# Note that if assigning a variable whose aggregation=SUM in the cross
# replica context, each replica is assigned with the value divided by the
# number of replicas.

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_READ,
            aggregation=tf.VariableAggregation.SUM)

    @tf.function(input_signature=[tf.TensorSpec(shape=(), dtype=tf.float32)])
    def update(self, value):
        self.v.assign_add(value)

export_dir = self.get_temp_dir()
# TODO(b/157621013): strategy.run doesn't work with tf.function with
# input_signature.
# value = strategy.experimental_distribute_values_from_function(
#     lambda ctx: tf.identity([3., 7.][ctx.replica_id_in_sync_group]))
with strategy.scope():
    m = Model()
    tf.saved_model.save(m, export_dir)
    self.evaluate(m.v.assign(10.))
    self.assertAllEqual(
        self.evaluate(strategy.experimental_local_results(m.v)), [5., 5.])
    del m
    # TODO(b/157621013): strategy.run doesn't work with tf.function with
    # input_signature.
    # self.evaluate(strategy.run(m.update, args=(value,)))
    # self.assertAllEqual(
    #     self.evaluate(strategy.experimental_local_results(m.v)), [8., 12.])

with strategy.scope():
    loaded = tf.saved_model.load(export_dir)
    self.evaluate(loaded.v.assign(10.))
    self.assertAllEqual(
        self.evaluate(strategy.experimental_local_results(loaded.v)),
        [5., 5.])
    # TODO(b/157621013): strategy.run doesn't work with tf.function with
    # input_signature.
    # self.evaluate(strategy.run(loaded.update, args=(value,)))
    # self.assertAllEqual(
    #     self.evaluate(strategy.experimental_local_results(loaded.v)),
    #     [8., 12.])
