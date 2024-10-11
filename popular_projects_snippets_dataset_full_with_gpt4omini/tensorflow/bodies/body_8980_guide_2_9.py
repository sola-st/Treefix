import numpy as np # pragma: no cover

class MockCheckOps:  # Mocking the check operations # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_equal_v2(actual, expected): # pragma: no cover
        assert np.array_equal(actual.numpy(), expected.numpy()), f'Assertion failed: {actual.numpy()} != {expected.numpy()}' # pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
class MockStrategy:  # Mocking the strategy # pragma: no cover
    def run(self, fn, args): return fn(args[0]) # pragma: no cover
    def reduce(self, reduction, values, axis): return tf.reduce_sum(values) # pragma: no cover

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
