import gast # pragma: no cover
import astor # pragma: no cover
import unittest.mock as mock # pragma: no cover

transformer = type('MockTransformer', (object,), {'Base': object}) # pragma: no cover
self = mock.MagicMock() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': mock.MagicMock(return_value=(gast.Module(body=[]), 'source_code'))}) # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': mock.MagicMock()}) # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': mock.MagicMock(return_value=mock.MagicMock()), 'Basic': type('MockBasic', (object,), {'ORIGIN': 'origin'})}) # pragma: no cover

import gast # pragma: no cover
from unittest import mock # pragma: no cover
import sys # pragma: no cover

transformer = type('MockTransformer', (object,), {'Base': object}) # pragma: no cover
self = mock.MagicMock() # pragma: no cover
self._simple_context = mock.MagicMock(return_value='simple_context') # pragma: no cover
self.assertEqual = mock.MagicMock() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': mock.MagicMock(return_value=(gast.Module(body=[gast.FunctionDef(name='test_fn', args=None, body=[gast.If(test=gast.Name(id='x', ctx=gast.Load()), body=[gast.Assign(targets=[gast.Name(id='x', ctx=gast.Store())], value=gast.Constant(value=1))], orelse=[]), gast.Pass()])]), 'source_code'))}) # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': mock.MagicMock()}) # pragma: no cover
anno = type('MockAnno', (object,), {'Basic': type('MockBasic', (object,), {'ORIGIN': 'origin'})(), 'getanno': mock.MagicMock(return_value=type('MockAnnoInstance', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})())}) # pragma: no cover
gast.Pass = mock.MagicMock(return_value=gast.Pass()) # pragma: no cover

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
