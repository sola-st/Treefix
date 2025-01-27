# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def test_fn(a, b, c, d, e):  # pylint: disable=unused-argument
    a = (lambda a, b, c=e: a + b + c)(d, 1, 2) + b

node, _ = self._parse_and_analyze(test_fn)

fn_node = node
scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('d', 'b', 'e'), ('a',))

lam_def_node = node.body[0].value.left.func

scope = anno.getanno(lam_def_node, anno.Static.SCOPE)
self.assertScopeIs(scope, ('e',), ())

scope = anno.getanno(lam_def_node, NodeAnno.BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b', 'c'), ())

scope = anno.getanno(lam_def_node, NodeAnno.ARGS_AND_BODY_SCOPE)
self.assertScopeIs(scope, ('a', 'b', 'c'), ())
self.assertSymbolSetsAre(('a', 'b', 'c'), scope.bound, 'BOUND')

scope = anno.getanno(lam_def_node.args, anno.Static.SCOPE)
self.assertSymbolSetsAre(
    ('a', 'b', 'c'), scope.params.keys(), 'lambda params')
