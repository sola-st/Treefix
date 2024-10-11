import gast # pragma: no cover
import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

transformer = type('MockTransformerBase', (object,), {'Base': object}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': unittest.TestCase().assertEqual})() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': lambda fn, future_features: (Mock(), '')})() # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': lambda node, source, filename, lineno, col_offset: None})() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, cls: type('Origin', (object,), {'loc': type('Loc', (object,), {'lineno': 102})()})(), 'Basic': type('Basic', (object,), {'ORIGIN': object})()})() # pragma: no cover
gast = Mock(Pass=lambda: gast.Pass()) # pragma: no cover

import gast # pragma: no cover
from unittest import TestCase # pragma: no cover

mock_transformer_base = type('MockTransformerBase', (object,), {'Base': object}) # pragma: no cover
transformer = mock_transformer_base # pragma: no cover
class MockSelf(TestCase): # pragma: no cover
    def _simple_context(self): # pragma: no cover
        return None # pragma: no cover
self = MockSelf() # pragma: no cover
class MockParser: # pragma: no cover
    @staticmethod # pragma: no cover
    def parse_entity(fn, future_features): # pragma: no cover
        node = gast.parse('def test_fn():\n    pass\n    if 1:\n        pass') # pragma: no cover
        return node, 'test_fn_source' # pragma: no cover
parser = MockParser() # pragma: no cover
class MockOriginInfo: # pragma: no cover
    @staticmethod # pragma: no cover
    def resolve(node, source, filename, lineno, col_offset): # pragma: no cover
        pass # pragma: no cover
origin_info = MockOriginInfo() # pragma: no cover
class MockAnno: # pragma: no cover
    class Basic: # pragma: no cover
        ORIGIN = 'ORIGIN' # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node, key): # pragma: no cover
        class Loc: # pragma: no cover
            lineno = 102 # pragma: no cover
        class Origin: # pragma: no cover
            loc = Loc() # pragma: no cover
        return Origin() # pragma: no cover
anno = MockAnno() # pragma: no cover
gast.Pass = lambda: gast.parse('pass').body[0] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

from l3.Runtime import _l_
class TestTransformer(transformer.Base):
    _l_(21506)


    def visit_If(self, node):
        _l_(21505)

        aux = gast.Pass()
        _l_(21504)
        exit(aux)

tr = TestTransformer(self._simple_context())
_l_(21507)

def test_fn():
    _l_(21512)

    x = 1
    _l_(21508)
    if x > 0:
        _l_(21510)

        x = 1
        _l_(21509)
    aux = x
    _l_(21511)
    exit(aux)

node, source = parser.parse_entity(test_fn, future_features=())
_l_(21513)
origin_info.resolve(node, source, 'test_file', 100, 0)
_l_(21514)
node = tr.visit(node)
_l_(21515)

created_pass_node = node.body[1]
_l_(21516)
# Takes the line number of the if statement.
self.assertEqual(
    anno.getanno(created_pass_node, anno.Basic.ORIGIN).loc.lineno, 102)
_l_(21517)
