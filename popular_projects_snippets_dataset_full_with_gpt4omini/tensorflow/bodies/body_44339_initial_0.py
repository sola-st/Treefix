import unittest # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
from l3.Runtime import _l_
def new_generator():
    _l_(9445)

    for i in range(5):
        _l_(9444)

        aux = i
        _l_(9443)
        exit(aux)

gen = new_generator()
_l_(9446)
def run_loop():
    _l_(9453)

    s = 0
    _l_(9447)

    def body(i):
        _l_(9450)

        nonlocal s
        _l_(9448)
        s = s * 10 + i
        _l_(9449)

    control_flow.for_stmt(
        gen,
        extra_test=lambda: False,  # Break before loop
        body=body,
        get_state=None,
        set_state=None,
        symbol_names=('s',),
        opts={})
    _l_(9451)
    aux = s
    _l_(9452)
    exit(aux)

self.assertEqual(run_loop(), 0)
_l_(9454)
self.assertEqual(run_loop(), 0)
_l_(9455)

self.assertEqual(next(gen), 0)
_l_(9456)

self.assertNoOpsCreated()
_l_(9457)
