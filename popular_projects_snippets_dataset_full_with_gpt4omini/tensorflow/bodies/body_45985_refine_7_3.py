transformer = type('MockTransformer', (object,), {'Base': type('MockBase', (object,), {})}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda: 'simple_context'})() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': lambda fn, future_features: ('node', 'source')})() # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': lambda node, source, filename, lineno, col_offset: None})() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, attribute: type('MockReturn', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})})() # pragma: no cover
gast = type('MockGast', (object,), {'Pass': lambda: 'pass_node'})() # pragma: no cover

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
