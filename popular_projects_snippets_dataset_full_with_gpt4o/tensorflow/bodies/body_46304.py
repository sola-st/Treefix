# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
b = int
c = int

def test_fn(a: b) -> c:
    exit(a)

node, _ = self._parse_and_analyze(test_fn)
fn_node = node

fn_scope = anno.getanno(fn_node, anno.Static.SCOPE)
self.assertScopeIs(fn_scope, ('b', 'c'), ('test_fn',))
self.assertSymbolSetsAre(('b', 'c'), fn_scope.annotations, 'annotations')

body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(body_scope, ('a',), ())
self.assertSymbolSetsAre((), body_scope.annotations, 'annotations')
