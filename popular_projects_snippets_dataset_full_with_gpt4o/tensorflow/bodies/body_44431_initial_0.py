control_flow = type('Mock', (object,), {'while_stmt': lambda test, body, get_state, set_state, symbol_names, opts: while_loop(test, body, get_state, set_state)}) # pragma: no cover
cond_fn = lambda s: s < 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
from l3.Runtime import _l_
def test_():
    _l_(21058)

    aux = cond_fn(s)
    _l_(21057)
    exit(aux)

def body():
    _l_(21061)

    nonlocal s
    _l_(21059)
    s += 1
    _l_(21060)

def set_state(loop_vars):
    _l_(21064)

    nonlocal s
    _l_(21062)
    s, = loop_vars
    _l_(21063)

s = constant_op.constant(0)
_l_(21065)
control_flow.while_stmt(
    test=test_,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={})
_l_(21066)
aux = s
_l_(21067)
exit(aux)
