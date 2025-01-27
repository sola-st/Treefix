# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a, b):
    a = []
    if b:
        a = []
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[0].targets[0], 1)
self.assertHasDefs(fn_body[1].test, 1)
self.assertHasDefs(fn_body[1].body[0].targets[0], 1)
self.assertHasDefs(fn_body[2].value, 2)

self.assertHasDefinedIn(fn_body[1], ('a', 'b'))
