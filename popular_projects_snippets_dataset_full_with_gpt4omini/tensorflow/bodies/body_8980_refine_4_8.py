import numpy as np # pragma: no cover

self = type('Mock', (), {'assertFalse': lambda x: None, 'strategy': type('MockStrategy', (), {'run': lambda f, args: args[0] + v, 'reduce': lambda op, val, axis: val})()})() # pragma: no cover
check_ops = type('MockCheckOps', (), {'assert_equal_v2': lambda x, y: None})() # pragma: no cover

class MockStrategy: pass # pragma: no cover
self = type('Mock', (), {'assertFalse': lambda x: None})() # pragma: no cover
self.strategy = MockStrategy() # pragma: no cover
self.strategy.run = lambda fn, args: (args[0] + v, args[0] - v) # pragma: no cover
self.strategy.reduce = lambda reduction, results, axis: results[0] + results[1] # pragma: no cover
check_ops = type('MockCheckOps', (), {'assert_equal_v2': lambda x, y: None})() # pragma: no cover

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
