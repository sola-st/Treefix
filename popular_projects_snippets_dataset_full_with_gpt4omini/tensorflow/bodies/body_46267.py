# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b, c):  # pylint: disable=unused-argument
    try:
        pass
    except:  # pylint: disable=bare-except
        b = c

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
self.assertScopeIs(
    anno.getanno(fn_node, NodeAnno.BODY_SCOPE), ('c',), ('b',))
