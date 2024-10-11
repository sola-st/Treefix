import gast # pragma: no cover
from unittest import TestCase # pragma: no cover
from ast import parse # pragma: no cover

transformer = type('MockTransformer', (object,), {'Base': object}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: 'dummy_context', 'assertEqual': TestCase().assertEqual})() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': lambda fn, features: (parse('test_fn()'), 'source')}) # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': lambda node, source, filename, lineno, offset: None}) # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, anno_type: type('MockAnnoType', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})(), 'Basic': type('MockBasic', (object,), {})})() # pragma: no cover

import gast # pragma: no cover
from unittest import TestCase # pragma: no cover
from unittest.mock import Mock # pragma: no cover

transformer = type('MockTransformer', (object,), {'Base': object}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': TestCase().assertEqual})() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': Mock(return_value=(gast.If(test=None, body=[], orelse=[]), 'source_code'))}) # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': Mock()})() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': Mock(return_value=type('MockAnnoInstance', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})()), 'Basic': type('Basic', (object,), {'ORIGIN': 'origin'})})() # pragma: no cover

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
