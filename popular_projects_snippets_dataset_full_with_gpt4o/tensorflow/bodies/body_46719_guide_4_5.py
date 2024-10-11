import ast # pragma: no cover
import types # pragma: no cover

global_a = True # pragma: no cover
global_b = None # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_parse_and_analyze': lambda self, fn: types.SimpleNamespace(body=ast.parse(''' # pragma: no cover
def test_fn(c): # pragma: no cover
    global global_a # pragma: no cover
    global global_b # pragma: no cover
    if global_a: # pragma: no cover
        global_b = c # pragma: no cover
    else: # pragma: no cover
        global_b = c # pragma: no cover
    aux = global_b # pragma: no cover
''').body[0].body), # pragma: no cover
    'assertHasLiveOut': lambda self, node, vars: print(f'assertHasLiveOut called with: {node}, {vars}'), # pragma: no cover
    'assertHasLiveIn': lambda self, node, vars: print(f'assertHasLiveIn called with: {node}, {vars}') # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

from l3.Runtime import _l_
def test_fn(c):
    _l_(20388)

    global global_a
    _l_(20382)
    global global_b
    _l_(20383)
    if global_a:
        _l_(20386)

        global_b = c
        _l_(20384)
    else:
        global_b = c
        _l_(20385)
    aux = global_b
    _l_(20387)
    exit(aux)

node = self._parse_and_analyze(test_fn)
_l_(20389)
fn_body = node.body
_l_(20390)
self.assertHasLiveOut(fn_body[2], ('global_b',))
_l_(20391)
self.assertHasLiveIn(fn_body[2], ('global_a', 'c'))
_l_(20392)
