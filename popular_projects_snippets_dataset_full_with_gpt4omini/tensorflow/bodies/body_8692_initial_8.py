tpu_strategy = type('MockTPUStrategy', (object,), {'TPUStrategy': type('MockTPUStrategyObj', (object,), {}), 'TPUStrategyV1': type('MockTPUStrategyV1Obj', (object,), {}), 'TPUStrategyV2': type('MockTPUStrategyV2Obj', (object,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
from l3.Runtime import _l_
aux = isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2))
_l_(9901)
exit(aux)
