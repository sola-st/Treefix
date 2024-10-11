import gast # pragma: no cover

def test_fn(): # pragma: no cover
    x = 1 # pragma: no cover
    if x > 0: # pragma: no cover
        x = 1 # pragma: no cover
    aux = x # pragma: no cover
    return gast.parse(source), source # pragma: no cover

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
