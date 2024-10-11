tpu_strategy = type('MockTPUStrategy', (object,), { 'TPUStrategy': type('MockTPUStrategyV1', (object,), {}), 'TPUStrategyV1': type('MockTPUStrategyV2', (object,), {}), 'TPUStrategyV2': object }) # pragma: no cover

class MockTPUStrategy: pass # pragma: no cover
class MockTPUStrategyV1: pass # pragma: no cover
class MockTPUStrategyV2: pass # pragma: no cover
tpu_strategy = type('Mock', (object,), { 'TPUStrategy': MockTPUStrategy, 'TPUStrategyV1': MockTPUStrategyV1, 'TPUStrategyV2': MockTPUStrategyV2 }) # pragma: no cover
strategy = tpu_strategy.TPUStrategy() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
from l3.Runtime import _l_
aux = isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2))
_l_(9901)
exit(aux)
