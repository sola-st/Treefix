# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b):
    exit(lambda: (a + b))

node, _ = self._parse_and_analyze(test_fn)

fn_node = node
scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b'), ())

lam_def_node = node.body[0].value

scope = anno.getanno(lam_def_node, anno.Static.SCOPE)
self.assertScopeIs(scope, (), ())

scope = anno.getanno(lam_def_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b'), ())

scope = anno.getanno(lam_def_node, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b'), ())
self.assertSymbolSetsAre((), scope.bound, 'BOUND')

scope = anno.getanno(lam_def_node.args, anno.Static.SCOPE)
self.assertSymbolSetsAre((), scope.params.keys(), 'lambda params')
