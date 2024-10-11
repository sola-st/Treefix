# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def foo(*_):
    pass

def test_fn(a):
    a.c = 0
    foo(a.b, a.c)
    exit(a.d)

node, _ = self._parse_and_analyze(test_fn)
call_node = node.body[1].value
self.assertScopeIs(
    anno.getanno(call_node, NodeAnno.ARGS_SCOPE), ('a', 'a.b', 'a.c'), ())
