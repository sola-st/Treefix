import gast # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import sys # pragma: no cover
sys.modules['transformer'] = Mock() # pragma: no cover
sys.modules['parser'] = Mock() # pragma: no cover
sys.modules['origin_info'] = Mock() # pragma: no cover
sys.modules['anno'] = Mock() # pragma: no cover

transformer = sys.modules['transformer'] # pragma: no cover
transformer.Base = type('MockTransformerBase', (object,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': lambda self, x, y: None})() # pragma: no cover
parser = sys.modules['parser'] # pragma: no cover
parser.parse_entity = lambda fn, future_features: (gast.Module(body=[gast.FunctionDef(body=[gast.Pass(), gast.Pass()])]), 'source_code') # pragma: no cover
origin_info = sys.modules['origin_info'] # pragma: no cover
origin_info.resolve = lambda node, source, filename, lineno, col_offset: None # pragma: no cover
anno = sys.modules['anno'] # pragma: no cover
anno.getanno = lambda node, key: type('MockAnno', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})() # pragma: no cover
anno.Basic = type('MockAnnoBasic', (object,), {'ORIGIN': 'origin'}) # pragma: no cover

import gast # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import sys # pragma: no cover
sys.modules['transformer'] = Mock() # pragma: no cover
sys.modules['parser'] = Mock() # pragma: no cover
sys.modules['origin_info'] = Mock() # pragma: no cover
sys.modules['anno'] = Mock() # pragma: no cover

transformer = sys.modules['transformer'] # pragma: no cover
transformer.Base = object # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': lambda self, x, y: None})() # pragma: no cover
parser = sys.modules['parser'] # pragma: no cover
parser.parse_entity = lambda fn, future_features: (gast.Module(body=[gast.FunctionDef(body=[gast.Pass(), gast.Pass()])]), 'source_code') # pragma: no cover
origin_info = sys.modules['origin_info'] # pragma: no cover
origin_info.resolve = lambda node, source, filename, lineno, col_offset: None # pragma: no cover
anno = sys.modules['anno'] # pragma: no cover
anno.getanno = lambda node, key: type('MockAnno', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})() # pragma: no cover
anno.Basic = type('MockAnnoBasic', (object,), {'ORIGIN': 'origin'}) # pragma: no cover

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
