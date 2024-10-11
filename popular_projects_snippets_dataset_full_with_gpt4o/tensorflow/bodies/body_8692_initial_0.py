import types # pragma: no cover

strategy = types.SimpleNamespace() # pragma: no cover
tpu_strategy = type('Mock', (object,), {'TPUStrategy': type('TPUStrategy', (object,), {}), 'TPUStrategyV1': type('TPUStrategyV1', (object,), {}), 'TPUStrategyV2': type('TPUStrategyV2', (object,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
from l3.Runtime import _l_
aux = isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2))
_l_(22265)
exit(aux)
