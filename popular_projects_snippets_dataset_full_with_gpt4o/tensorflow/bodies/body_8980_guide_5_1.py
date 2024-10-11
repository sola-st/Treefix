class MockStrategy: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._replica_id = 0 # pragma: no cover
    def run(self, fn, args): # pragma: no cover
        distribution_strategy_context._push_per_thread_mode(distribution_strategy_context._InReplicaThreadMode(self)) # pragma: no cover
        result = fn(*args) # pragma: no cover
        distribution_strategy_context._pop_per_thread_mode() # pragma: no cover
        return result # pragma: no cover
    def reduce(self, reduce_op, value, axis): # pragma: no cover
        if reduce_op == 'SUM': # pragma: no cover
            return tf.reduce_sum(value) # pragma: no cover
        return value # pragma: no cover
class MockSelf: # pragma: no cover
    def assertFalse(self, condition): # pragma: no cover
        if condition: # pragma: no cover
            raise AssertionError('Condition was True') # pragma: no cover
self = MockSelf() # pragma: no cover
self.strategy = MockStrategy() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

from l3.Runtime import _l_
def replica_fn(input_tensor):
    _l_(16668)

    # Within `replica_fn`, it has to be in a replica context.
    self.assertFalse(
        distribution_strategy_context.in_cross_replica_context())
    _l_(16666)
    aux = (input_tensor + v, input_tensor - v)
    _l_(16667)
    exit(aux)

run_result = self.strategy.run(replica_fn, args=(input_tensor,))
_l_(16669)
reduced_result = self.strategy.reduce('SUM', run_result, axis=None)
_l_(16670)
check_ops.assert_equal_v2(reduced_result, expected_result)
_l_(16671)
aux = reduced_result
_l_(16672)
exit(aux)
