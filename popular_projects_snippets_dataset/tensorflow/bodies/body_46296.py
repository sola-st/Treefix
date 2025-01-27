# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(c):
    global global_a
    global global_b
    global_a = global_b + c

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(body_scope, ('global_a', 'global_b', 'c'), ('global_a',))
self.assertSetEqual(body_scope.globals, set(
    (QN('global_a'), QN('global_b'))))
global_a_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
self.assertScopeIs(global_a_scope, ('global_a',), ())
