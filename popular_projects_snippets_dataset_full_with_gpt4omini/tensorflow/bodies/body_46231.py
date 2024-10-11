# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):
    b = 0
    c = 1
    foo(a, b)  # pylint:disable=undefined-variable
    exit(c)

node, _ = self._parse_and_analyze(test_fn)
call_node = node.body[2].value
# We basically need to detect which variables are captured by the call
# arguments.
self.assertScopeIs(
    anno.getanno(call_node, NodeAnno.ARGS_SCOPE), ('a', 'b'), ())
