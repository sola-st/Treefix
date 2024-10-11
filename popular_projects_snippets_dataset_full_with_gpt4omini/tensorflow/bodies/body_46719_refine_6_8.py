class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
global_a = True # pragma: no cover

class Mock: # pragma: no cover
    def _parse_and_analyze(self, func): # pragma: no cover
        return type('Node', (object,), {'body': [None, None, None]})() # pragma: no cover
self = Mock() # pragma: no cover
global_a = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

from l3.Runtime import _l_
def test_fn(c):
    _l_(7329)

    global global_a
    _l_(7323)
    global global_b
    _l_(7324)
    if global_a:
        _l_(7327)

        global_b = c
        _l_(7325)
    else:
        global_b = c
        _l_(7326)
    aux = global_b
    _l_(7328)
    exit(aux)

node = self._parse_and_analyze(test_fn)
_l_(7330)
fn_body = node.body
_l_(7331)
self.assertHasLiveOut(fn_body[2], ('global_b',))
_l_(7332)
self.assertHasLiveIn(fn_body[2], ('global_a', 'c'))
_l_(7333)
