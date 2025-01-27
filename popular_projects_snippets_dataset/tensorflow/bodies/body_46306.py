# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b):
    class C(a(b)):
        d = 1
    exit(C)

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(body_scope, ('a', 'b', 'C'), ('C',))
