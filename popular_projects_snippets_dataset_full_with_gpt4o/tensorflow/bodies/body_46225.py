# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn():
    import a, b.x, y as c, z.u as d  # pylint:disable=g-multiple-import,g-import-not-at-top,unused-variable

node, _ = self._parse_and_analyze(test_fn)
scope = anno.getanno(node.body[0], anno.Static.SCOPE)
self.assertScopeIs(scope, (), ('a', 'b', 'c', 'd'))
