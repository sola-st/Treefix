import numpy as np # pragma: no cover

class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
class MockCheckOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def assert_equal_v2(a, b):# pragma: no cover
        tf.debugging.assert_equal(a, b)# pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
class MockStrategy:# pragma: no cover
    def run(self, fn, args):# pragma: no cover
        return fn(*args)# pragma: no cover
    def reduce(self, reduction, value, axis):# pragma: no cover
        return tf.reduce_sum(value, axis=axis)# pragma: no cover
self.strategy = MockStrategy() # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
class MockStrategy:# pragma: no cover
    def run(self, fn, args):# pragma: no cover
        return fn(*args)# pragma: no cover
    def reduce(self, reduction, values, axis):# pragma: no cover
        return tf.add_n(values)# pragma: no cover
self.strategy = MockStrategy() # pragma: no cover
class MockCheckOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def assert_equal_v2(a, b):# pragma: no cover
        tf.debugging.assert_equal(a, b)# pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
distribution_strategy_context = type('Mock', (object,), {'in_cross_replica_context': lambda: False})() # pragma: no cover

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
