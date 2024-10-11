import sys # pragma: no cover

global_a = True # pragma: no cover
global_b = None # pragma: no cover
def mock_assertHasLiveOut(body, vars): pass # pragma: no cover
def mock_assertHasLiveIn(body, vars): pass # pragma: no cover
def mock_parse_and_analyze(fn): # pragma: no cover
    class MockNode: # pragma: no cover
        def __init__(self, body): # pragma: no cover
            self.body = body # pragma: no cover
    return MockNode(fn.__code__.co_code) # pragma: no cover
self = type('MockSelf', (object,), {'_parse_and_analyze': mock_parse_and_analyze, 'assertHasLiveOut': mock_assertHasLiveOut, 'assertHasLiveIn': mock_assertHasLiveIn})() # pragma: no cover

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
