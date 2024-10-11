import gast # pragma: no cover
import ast # pragma: no cover
from unittest import TestCase # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockBase(object): pass # pragma: no cover
transformer = type('MockTransformer', (MockBase,), {'Base': MockBase}) # pragma: no cover
self = TestCase() # pragma: no cover
parser = MagicMock() # pragma: no cover
origin_info = MagicMock() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': MagicMock(return_value=MagicMock(loc=MagicMock(lineno=102)))}) # pragma: no cover
gast = type('MockGast', (object,), {'Pass': MagicMock()}) # pragma: no cover

import gast # pragma: no cover
from unittest import TestCase # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockBase: pass # pragma: no cover
class TestTransformer(MockBase): # pragma: no cover
    def visit_If(self, node): # pragma: no cover
        return gast.Pass() # pragma: no cover
tr = TestTransformer() # pragma: no cover
self = TestCase() # pragma: no cover
self._simple_context = lambda: {} # pragma: no cover
parser = MagicMock() # pragma: no cover
parser.parse_entity = lambda fn, future_features: ('node', 'source') # pragma: no cover
origin_info = MagicMock() # pragma: no cover
origin_info.resolve = lambda node, source, filename, lineno, col_offset: None # pragma: no cover
anno = type('MockAnno', (object,), {}) # pragma: no cover
anno.getanno = lambda node, key: type('MockLoc', (object,), {'lineno': 102})() # pragma: no cover
gast = type('MockGast', (object,), {'Pass': lambda: 'pass_node'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

from l3.Runtime import _l_
class TestTransformer(transformer.Base):
    _l_(8967)


    def visit_If(self, node):
        _l_(8966)

        aux = gast.Pass()
        _l_(8965)
        exit(aux)

tr = TestTransformer(self._simple_context())
_l_(8968)

def test_fn():
    _l_(8973)

    x = 1
    _l_(8969)
    if x > 0:
        _l_(8971)

        x = 1
        _l_(8970)
    aux = x
    _l_(8972)
    exit(aux)

node, source = parser.parse_entity(test_fn, future_features=())
_l_(8974)
origin_info.resolve(node, source, 'test_file', 100, 0)
_l_(8975)
node = tr.visit(node)
_l_(8976)

created_pass_node = node.body[1]
_l_(8977)
# Takes the line number of the if statement.
self.assertEqual(
    anno.getanno(created_pass_node, anno.Basic.ORIGIN).loc.lineno, 102)
_l_(8978)
