# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a, b):  # pylint:disable=unused-argument
    a = []
    if b:
        try:
            pass
        except:  # pylint:disable=bare-except
            pass
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefinedIn(fn_body[1], ('a', 'b'))
self.assertHasDefinedIn(fn_body[1].body[0], ('a', 'b'))
