tpu_strategy = type('MockTPUStrategy', (object,), {'TPUStrategy': type('Mock', (object,), {}), 'TPUStrategyV1': type('Mock', (object,), {}), 'TPUStrategyV2': type('Mock', (object,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
from l3.Runtime import _l_
aux = isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2))
_l_(9901)
exit(aux)
