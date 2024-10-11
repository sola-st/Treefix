# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b, c):  # pylint: disable=unused-argument
    raise b

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
self.assertScopeIs(anno.getanno(fn_node, NodeAnno.BODY_SCOPE), ('b',), ())
self.assertScopeIs(
    anno.getanno(node.body[0], anno.Static.SCOPE), ('b',), ())
