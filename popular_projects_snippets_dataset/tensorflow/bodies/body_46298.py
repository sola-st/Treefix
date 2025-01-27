# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
nonlocal_a = 3
nonlocal_b = 13

def test_fn(c):
    nonlocal nonlocal_a
    nonlocal nonlocal_b
    nonlocal_a = nonlocal_b + c

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(
    body_scope, ('nonlocal_a', 'nonlocal_b', 'c'), ('nonlocal_a',))
nonlocal_a_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
self.assertScopeIs(nonlocal_a_scope, ('nonlocal_a',), ())
