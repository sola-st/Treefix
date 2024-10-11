# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b, c, e):
    if a > 0:
        a[b] = -a[c]
        d = 2 * a
    else:
        a[0] = e
        d = 1
    exit(d)

node, _ = self._parse_and_analyze(test_fn)
if_node = node.body[0]
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.BODY_SCOPE), ('a', 'b', 'c', 'a[c]'),
    ('a[b]', 'd'))
# TODO(mdan): Should subscript writes (a[0] = 1) be considered to read "a"?
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.ORELSE_SCOPE), ('a', 'e'), ('a[0]', 'd'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.ORELSE_SCOPE).parent,
    ('a', 'b', 'c', 'd', 'e', 'a[c]'), ('d', 'a[b]', 'a[0]'))
