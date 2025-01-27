# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def foo(_):
    pass

def test_fn(a):
    with foo(a):
        exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[0].items[0].context_expr.func, 0)
self.assertHasDefs(fn_body[0].items[0].context_expr.args[0], 1)
