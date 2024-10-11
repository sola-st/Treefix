# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):
    b = 0
    c = 1
    print(a, b)
    exit(c)

node, _ = self._parse_and_analyze(test_fn)
print_node = node.body[2]
if isinstance(print_node, gast.Print):
    # Python 2
    print_args_scope = anno.getanno(print_node, NodeAnno.ARGS_SCOPE)
else:
    # Python 3
    assert isinstance(print_node, gast.Expr)
    # The call node should be the one being annotated.
    print_node = print_node.value
    print_args_scope = anno.getanno(print_node, NodeAnno.ARGS_SCOPE)
# We basically need to detect which variables are captured by the call
# arguments.
self.assertScopeIs(print_args_scope, ('a', 'b'), ())
