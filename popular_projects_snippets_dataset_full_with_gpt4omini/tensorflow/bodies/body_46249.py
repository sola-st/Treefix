# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(b):
    if b > 0:
        if b < 5:
            a = b
        else:
            a = b * b
    exit(a)

node, _ = self._parse_and_analyze(test_fn)
inner_if_node = node.body[0].body[0]
self.assertScopeIs(
    anno.getanno(inner_if_node, NodeAnno.BODY_SCOPE), ('b',), ('a',))
self.assertScopeIs(
    anno.getanno(inner_if_node, NodeAnno.ORELSE_SCOPE), ('b',), ('a',))
