transformer = type('MockTransformer', (object,), {'Base': object}) # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': lambda self, a, b: None})() # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': lambda fn, features: (gast.FunctionDef(name='test_fn', args=None, body=[], decorator_list=[], returns=None), 'test_fn_code')})() # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': lambda node, source, fname, line, col: None})() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, ann: type('MockAnnoInstance', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})(), 'Basic': type('MockBasic', (object,), {})()})() # pragma: no cover

class MockTransformerBase: # pragma: no cover
    def __init__(self, context=None): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'_simple_context': lambda self: None, 'assertEqual': lambda self, x, y: None})() # pragma: no cover
 # pragma: no cover
def mock_parse_entity(func, future_features): # pragma: no cover
    node = gast.FunctionDef(name='test_fn', args=None, body=[gast.Expr(value=gast.Call(func=gast.Name(id='exit', ctx=gast.Load()), args=[gast.Constant(value=1)], keywords=[])), gast.Pass()], decorator_list=[], returns=None) # pragma: no cover
    source = '' # pragma: no cover
    return node, source # pragma: no cover
parser = type('MockParser', (object,), {'parse_entity': mock_parse_entity})() # pragma: no cover
 # pragma: no cover
origin_info = type('MockOriginInfo', (object,), {'resolve': lambda node, source, filename, lineno, col_offset: None})() # pragma: no cover
 # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, key: type('MockAnnoInstance', (object,), {'loc': type('MockLoc', (object,), {'lineno': 102})()})(), 'Basic': type('Basic', (object,), {})})() # pragma: no cover

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
