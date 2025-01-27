# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):
    b = a
    for _ in a:
        c = b
        b -= 1
    exit((b, c))

node, _ = self._parse_and_analyze(test_fn)
for_node = node.body[1]
self.assertScopeIs(
    anno.getanno(for_node, NodeAnno.ITERATE_SCOPE), (), ('_'))
self.assertScopeIs(
    anno.getanno(for_node, NodeAnno.BODY_SCOPE), ('b',), ('b', 'c'))
self.assertScopeIs(
    anno.getanno(for_node, NodeAnno.BODY_SCOPE).parent, ('a', 'b', 'c'),
    ('b', 'c', '_'))
