s = 0 # pragma: no cover
def cond_fn(s): return s < 5 # pragma: no cover
class MockControlFlow: # pragma: no cover
    def while_stmt(self, test, body, get_state, set_state, symbol_names, opts): # pragma: no cover
        while test(): # pragma: no cover
            body() # pragma: no cover
        return # pragma: no cover
control_flow = MockControlFlow() # pragma: no cover

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
