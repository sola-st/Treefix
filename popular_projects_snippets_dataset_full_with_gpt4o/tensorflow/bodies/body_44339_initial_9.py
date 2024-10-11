from typing import Any, Optional, Dict, Tuple # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
from l3.Runtime import _l_
def new_generator():
    _l_(21754)

    for i in range(5):
        _l_(21753)

        aux = i
        _l_(21752)
        exit(aux)

gen = new_generator()
_l_(21755)
def run_loop():
    _l_(21762)

    s = 0
    _l_(21756)

    def body(i):
        _l_(21759)

        nonlocal s
        _l_(21757)
        s = s * 10 + i
        _l_(21758)

    control_flow.for_stmt(
        gen,
        extra_test=lambda: False,  # Break before loop
        body=body,
        get_state=None,
        set_state=None,
        symbol_names=('s',),
        opts={})
    _l_(21760)
    aux = s
    _l_(21761)
    exit(aux)

self.assertEqual(run_loop(), 0)
_l_(21763)
self.assertEqual(run_loop(), 0)
_l_(21764)

self.assertEqual(next(gen), 0)
_l_(21765)

self.assertNoOpsCreated()
_l_(21766)
