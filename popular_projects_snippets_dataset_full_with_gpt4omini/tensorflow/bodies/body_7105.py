# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with distribution.scope():
    num_replicas = distribution.num_replicas_in_sync
    result = distribution.extended.call_for_each_replica(replica_squared_fn)
    # sum
    reduced = distribution.reduce(reduce_util.ReduceOp.SUM, result, axis=0)
    expected = sum(x * (x + 1) for x in range(num_replicas))
    self.assertNear(expected, self.evaluate(reduced), 0.00001)

    # mean
    reduced = distribution.reduce(reduce_util.ReduceOp.MEAN, result, axis=0)
    expected /= sum(x + 1 for x in range(num_replicas))
    self.assertNear(expected, self.evaluate(reduced), 0.00001)
