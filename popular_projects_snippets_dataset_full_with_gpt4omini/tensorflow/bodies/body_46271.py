# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b):
    a += b

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
self.assertScopeIs(
    anno.getanno(fn_node, NodeAnno.BODY_SCOPE), ('a', 'b'), ('a'))
