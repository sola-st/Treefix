# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(x):
    if x > 0:
        x = -x
        y = 2 * x
        z = -y
    else:
        x = 2 * x
        y = -x
        u = -y
    exit((z, u))

node, _ = self._parse_and_analyze(test_fn)
if_node = node.body[0]
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.BODY_SCOPE), ('x', 'y'), ('x', 'y', 'z'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.BODY_SCOPE).parent, ('x', 'y', 'z', 'u'),
    ('x', 'y', 'z', 'u'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.ORELSE_SCOPE), ('x', 'y'),
    ('x', 'y', 'u'))
self.assertScopeIs(
    anno.getanno(if_node, NodeAnno.ORELSE_SCOPE).parent,
    ('x', 'y', 'z', 'u'), ('x', 'y', 'z', 'u'))
