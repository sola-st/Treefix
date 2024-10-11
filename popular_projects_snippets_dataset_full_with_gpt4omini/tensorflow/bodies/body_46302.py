# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
b = int

def test_fn():
    a: b
    exit(a)

node, _ = self._parse_and_analyze(test_fn)
fn_node = node

body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(body_scope, ('b', 'a'), ('a',))
self.assertSymbolSetsAre(('b',), body_scope.annotations, 'annotations')

ann_assign_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
self.assertScopeIs(ann_assign_scope, ('b',), ('a',))
self.assertSymbolSetsAre(
    ('b',), ann_assign_scope.annotations, 'annotations')
