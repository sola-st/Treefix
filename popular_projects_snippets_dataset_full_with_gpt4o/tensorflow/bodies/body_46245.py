# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):
    if a > 0:
        a.b = -a.c
        d = 2 * a
    else:
        a.b = a.c
        d = 1
    exit(d)

node, _ = self._parse_and_analyze(test_fn)
if_node = node.body[0]
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.BODY_SCOPE), ('a', 'a.c'), ('a.b', 'd'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.ORELSE_SCOPE), ('a', 'a.c'),
    ('a.b', 'd'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.BODY_SCOPE).parent, ('a', 'a.c', 'd'),
    ('a.b', 'd'))
