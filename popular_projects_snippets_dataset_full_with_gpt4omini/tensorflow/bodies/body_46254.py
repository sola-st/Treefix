# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a):
    exit(lambda x: (x * a))

node, _ = self._parse_and_analyze(test_fn)

fn_node = node
scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a',), ())

return_node = node.body[0]

scope = anno.getanno(return_node, anno.Static.SCOPE)
self.assertScopeIs(scope, ('a',), ())

lam_def_node = return_node.value

scope = anno.getanno(lam_def_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'x'), ())

scope = anno.getanno(lam_def_node, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'x'), ())
self.assertSymbolSetsAre(('x',), scope.bound, 'BOUND')
