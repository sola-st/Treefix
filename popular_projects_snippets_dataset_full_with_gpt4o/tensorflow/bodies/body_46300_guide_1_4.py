import ast # pragma: no cover
from unittest import TestCase # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import inspect # pragma: no cover

def parse_and_analyze(fn): # pragma: no cover
    class Analyzer(ast.NodeVisitor): # pragma: no cover
        def __init__(self): # pragma: no cover
            self.body_scope = mock_scope(('b', 'c', 'a'), ('a',)) # pragma: no cover
            self.ann_assign_scope = mock_scope(('b', 'c'), ('a',)) # pragma: no cover
        def visit_FunctionDef(self, node): # pragma: no cover
            fn_scope[node] = self.body_scope # pragma: no cover
            fn_scope[node.body[0]] = self.ann_assign_scope # pragma: no cover
    analyzer = Analyzer() # pragma: no cover
    fn_scope = {} # pragma: no cover
    tree = ast.parse(inspect.getsource(fn)) # pragma: no cover
    analyzer.visit(tree) # pragma: no cover
    return tree.body[0], fn_scope # pragma: no cover
 # pragma: no cover
def mock_scope(defined, ref): # pragma: no cover
    scope = Mock() # pragma: no cover
    scope.defined = defined # pragma: no cover
    scope.ref = ref # pragma: no cover
    scope.annotations = ('b',) # pragma: no cover
    return scope # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (TestCase,), { # pragma: no cover
    '_parse_and_analyze': lambda self, fn: parse_and_analyze(fn), # pragma: no cover
    'assertScopeIs': lambda self, scope, defined, ref: print(f'Scope defined: {scope.defined}, referenced: {scope.ref}'), # pragma: no cover
    'assertSymbolSetsAre': lambda self, syms, annotations, ann_type: print(f'Assertions passed: {syms == annotations}') # pragma: no cover
})() # pragma: no cover
anno = type('anno', (), { # pragma: no cover
    'getanno': lambda node, key: node.annotations[key] if key in node.annotations else None, # pragma: no cover
    'Static': type('Static', (), { 'SCOPE': 'scope' }) # pragma: no cover
}) # pragma: no cover
NodeAnno = type('NodeAnno', (), { # pragma: no cover
    'BODY_SCOPE': 'body_scope' # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
from l3.Runtime import _l_
b = int
_l_(17999)

def test_fn(c):
    _l_(18002)

    a: b = c
    _l_(18000)
    aux = a
    _l_(18001)
    exit(aux)

node, _ = self._parse_and_analyze(test_fn)
_l_(18003)
fn_node = node
_l_(18004)

body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
_l_(18005)
self.assertScopeIs(body_scope, ('b', 'c', 'a'), ('a',))
_l_(18006)
self.assertSymbolSetsAre(('b',), body_scope.annotations, 'annotations')
_l_(18007)

ann_assign_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
_l_(18008)
self.assertScopeIs(ann_assign_scope, ('b', 'c'), ('a',))
_l_(18009)
self.assertSymbolSetsAre(
    ('b',), ann_assign_scope.annotations, 'annotations')
_l_(18010)
