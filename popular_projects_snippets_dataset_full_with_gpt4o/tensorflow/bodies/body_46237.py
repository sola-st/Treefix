# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def foo(*_):
    pass

def test_fn(a):
    b = 1
    c = 2
    foo(a[0], a[b])
    exit(a[c])

node, _ = self._parse_and_analyze(test_fn)
call_node = node.body[2].value
self.assertScopeIs(
    anno.getanno(call_node, NodeAnno.ARGS_SCOPE),
    ('a', 'a[0]', 'a[b]', 'b'), ())
