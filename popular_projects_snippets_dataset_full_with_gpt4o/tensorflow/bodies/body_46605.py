# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a, b):
    a = []
    if b:
        try:
            if b:
                a = []
        except TestException:  # pylint:disable=undefined-variable,unused-variable
            pass
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefinedIn(fn_body[1], ('a', 'b'))
self.assertHasDefinedIn(fn_body[1].body[0], ('a', 'b'))
# Note: `TestException` and `e` are not tracked.
self.assertHasDefinedIn(fn_body[1].body[0].body[0], ('a', 'b'))
