control_flow = type('Mock', (object,), {'while_stmt': lambda test, body, get_state, set_state, symbol_names, opts: None}) # pragma: no cover
cond_fn = lambda s: s < 10 # pragma: no cover

class StateContainer:  # to hold the state variable 's' # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
 # pragma: no cover
state_container = StateContainer() # pragma: no cover
control_flow = type('Mock', (object,), {'while_stmt': lambda test, body, get_state, set_state, symbol_names, opts: None}) # pragma: no cover
def cond_fn(s): return s < 10 # pragma: no cover
 # pragma: no cover
def test_(): # pragma: no cover
    return cond_fn(state_container.s) # pragma: no cover
 # pragma: no cover
def body(): # pragma: no cover
    state_container.s += 1 # pragma: no cover
 # pragma: no cover
def set_state(loop_vars): # pragma: no cover
    state_container.s, = loop_vars # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
from l3.Runtime import _l_
def test_():
    _l_(7885)

    aux = cond_fn(s)
    _l_(7884)
    exit(aux)

def body():
    _l_(7888)

    nonlocal s
    _l_(7886)
    s += 1
    _l_(7887)

def set_state(loop_vars):
    _l_(7891)

    nonlocal s
    _l_(7889)
    s, = loop_vars
    _l_(7890)

s = constant_op.constant(0)
_l_(7892)
control_flow.while_stmt(
    test=test_,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={})
_l_(7893)
aux = s
_l_(7894)
exit(aux)
