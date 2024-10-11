# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn():
    try:
        raise ValueError()
    except ValueError:
        a = None
    if a:  # pylint:disable=using-constant-test
        a = None
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[1].test, 1)
self.assertHasDefs(fn_body[1].body[0].targets[0], 1)
self.assertHasDefs(fn_body[2].value, 2)

self.assertHasDefinedIn(fn_body[1], ('a',))
