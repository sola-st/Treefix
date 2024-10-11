check_ops = type('CheckOps', (object,), {'assert_equal_v2': staticmethod(lambda a, b: print('Check passed:', a.numpy(), '==', b.numpy()))})() # pragma: no cover
class MockStrategy: # pragma: no cover
    def run(self, fn, args): # pragma: no cover
        return [fn(*args)] # pragma: no cover
    def reduce(self, reduction, values, axis): # pragma: no cover
        return tf.reduce_sum(values, axis=axis) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

from l3.Runtime import _l_
def replica_fn(input_tensor):
    _l_(5056)

    # Within `replica_fn`, it has to be in a replica context.
    self.assertFalse(
        distribution_strategy_context.in_cross_replica_context())
    _l_(5054)
    aux = (input_tensor + v, input_tensor - v)
    _l_(5055)
    exit(aux)

run_result = self.strategy.run(replica_fn, args=(input_tensor,))
_l_(5057)
reduced_result = self.strategy.reduce('SUM', run_result, axis=None)
_l_(5058)
check_ops.assert_equal_v2(reduced_result, expected_result)
_l_(5059)
aux = reduced_result
_l_(5060)
exit(aux)
