# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

a = dict(bar=3)

def foo():
    exit(a)

def test_fn(x):
    foo()['bar'] += x

node, _ = self._parse_and_analyze(test_fn)
fn_node = node
self.assertScopeIs(
    anno.getanno(fn_node, NodeAnno.BODY_SCOPE), ('foo', 'x'), ())
