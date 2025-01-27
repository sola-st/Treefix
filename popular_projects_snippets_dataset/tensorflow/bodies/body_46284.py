# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b, c, d, e, f):  # pylint: disable=unused-argument
    a = lambda a, b: d(lambda b=f: a + b + c)  # pylint: disable=undefined-variable

node, _ = self._parse_and_analyze(test_fn)

fn_node = node
scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('d', 'c', 'f'), ('a',))

outer_lam_def = node.body[0].value

scope = anno.getanno(outer_lam_def, anno.Static.SCOPE)
self.assertScopeIs(scope, (), ())

scope = anno.getanno(outer_lam_def, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('d', 'f', 'a', 'c'), ())

scope = anno.getanno(outer_lam_def, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('d', 'f', 'a', 'c'), ())
self.assertSymbolSetsAre(('a', 'b'), scope.bound, 'BOUND')

scope = anno.getanno(outer_lam_def.args, anno.Static.SCOPE)
self.assertSymbolSetsAre(('a', 'b'), scope.params.keys(), 'lambda params')

inner_lam_def = outer_lam_def.body.args[0]

scope = anno.getanno(inner_lam_def, anno.Static.SCOPE)
self.assertScopeIs(scope, ('f',), ())

scope = anno.getanno(inner_lam_def, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b', 'c'), ())

scope = anno.getanno(inner_lam_def, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b', 'c'), ())
self.assertSymbolSetsAre(('b',), scope.bound, 'BOUND')

scope = anno.getanno(inner_lam_def.args, anno.Static.SCOPE)
self.assertSymbolSetsAre(('b',), scope.params.keys(), 'lambda params')
