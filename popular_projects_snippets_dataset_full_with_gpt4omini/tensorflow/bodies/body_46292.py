# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b):
    b += [c for c in a]  # pylint:disable=unused-variable

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(body_scope, ('a', 'b'), ('b',))
