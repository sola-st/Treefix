import numpy as np # pragma: no cover

self = type('Mock', (object,), {'assertFalse': lambda x: None, 'strategy': type('StrategyMock', (object,), {'run': lambda fn, args: fn(*args), 'reduce': lambda mode, result, axis: (result[0] + result[1]) * 2})})() # pragma: no cover
distribution_strategy_context = type('Mock', (object,), {'in_cross_replica_context': lambda: False})() # pragma: no cover

import numpy as np # pragma: no cover

distribution_strategy_context = type('Mock', (object,), {'in_cross_replica_context': lambda: False})() # pragma: no cover
self = type('Mock', (object,), {'assertFalse': lambda x: None, 'strategy': type('MockStrategy', (object,), {'run': lambda fn, args: fn(*args), 'reduce': lambda mode, result, axis: (result[0] + result[1]) * 2})()})() # pragma: no cover

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
