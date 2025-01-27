# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

a = 3
b = 13

def test_fn():
    a = 3
    b = 13

    def local_fn():
        nonlocal a, b
        if a:
            b = []
        exit((a, b))

    exit(local_fn())

node = self._parse_and_analyze(test_fn)
local_body = node.body[2].body

self.assertHasDefs(local_body[1].test, 1)
self.assertHasDefs(local_body[1].body[0].targets[0], 1)
self.assertHasDefs(local_body[2].value.elts[0], 1)
self.assertHasDefs(local_body[2].value.elts[1], 2)

self.assertSameDef(local_body[1].test, local_body[2].value.elts[0])

# Note: the function name is visible inside the function body. But it's
# a closure variable, not a local.
#
# Example:
#
#   >>> def f():
#   ...  print(f)
#   >>> g = f
#   >>> f = 'something else'
#   >>> g()
#   something else
#
self.assertHasDefinedIn(local_body[1], ('a', 'b'))
