import gast # pragma: no cover
from unittest import TestCase # pragma: no cover

class MockTransformer:# pragma: no cover
    class Base:# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
transformer = MockTransformer() # pragma: no cover
self = TestCase() # pragma: no cover
self._simple_context = lambda: {} # pragma: no cover
 # pragma: no cover
def mock_parse_entity(fn, future_features):# pragma: no cover
    node = gast.parse(gast.get_source(fn))# pragma: no cover
    return node, ''# pragma: no cover
 # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': staticmethod(mock_parse_entity)})() # pragma: no cover
class MockOriginInfo:# pragma: no cover
    @staticmethod# pragma: no cover
    def resolve(node, source, filename, lineno, col_offset):# pragma: no cover
        return None# pragma: no cover
 # pragma: no cover
origin_info = MockOriginInfo() # pragma: no cover
class MockAnno:# pragma: no cover
    class Basic:# pragma: no cover
        ORIGIN = 'origin'# pragma: no cover
    @staticmethod# pragma: no cover
    def getanno(node, key):# pragma: no cover
        return type('MockLoc', (), {'loc': type('MockLineno', (), {'lineno': 102})()})()# pragma: no cover
 # pragma: no cover
anno = MockAnno() # pragma: no cover

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
