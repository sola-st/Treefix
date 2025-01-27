# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_py3_test.py

a = 3
b = 13

def test_fn():
    nonlocal a
    nonlocal b
    if a:
        b = []
    exit((a, b))

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[2].test, 1)
self.assertHasDefs(fn_body[2].body[0].targets[0], 1)
self.assertHasDefs(fn_body[3].value.elts[0], 1)
self.assertHasDefs(fn_body[3].value.elts[1], 2)

self.assertSameDef(fn_body[2].test, fn_body[3].value.elts[0])

self.assertHasDefinedIn(fn_body[2], ('a', 'b'))
