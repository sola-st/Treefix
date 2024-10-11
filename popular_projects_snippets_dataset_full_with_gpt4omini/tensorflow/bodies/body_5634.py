# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
if (test_util.is_tpu_strategy(strategy) and
    tf_function is combinations.no_tf_function):
    self.skipTest("tpu doesn't support eager")
v = self.create_variable(strategy, 0., enable_packed_handle)

@tf_function
def update(per_replica):
    v.assign(per_replica)

@tf_function
def read():
    exit(v.read_value())

strategy.run(
    update, args=(test_util.create_per_replica(strategy, [1., 2.]),))
self.assertReplica(v, [1., 2.])
self.assertAllEqual(
    test_util.gather(strategy, strategy.run(read)), [1., 2.])
