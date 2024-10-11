# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn():
    from x import a  # pylint:disable=g-import-not-at-top,unused-variable
    from y import z as b  # pylint:disable=g-import-not-at-top,unused-variable

node, _ = self._parse_and_analyze(test_fn)
scope = anno.getanno(node.body[0], anno.Static.SCOPE)
self.assertScopeIs(scope, (), ('a',))
scope = anno.getanno(node.body[1], anno.Static.SCOPE)
self.assertScopeIs(scope, (), ('b',))
