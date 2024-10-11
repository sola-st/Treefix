# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):

    def f(x):
        y = x * x
        exit(y)

    exit(f(a))

node, _ = self._parse_and_analyze(test_fn)

fn_node = node
scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'f'), ('f',))

fn_def_node = node.body[0]

scope = anno.getanno(fn_def_node, anno.Static.SCOPE)
self.assertScopeIs(scope, (), ('f'))

scope = anno.getanno(fn_def_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('x', 'y'), ('y',))

scope = anno.getanno(fn_def_node, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('x', 'y'), ('y',))
self.assertSymbolSetsAre(('x', 'y'), scope.bound, 'BOUND')
