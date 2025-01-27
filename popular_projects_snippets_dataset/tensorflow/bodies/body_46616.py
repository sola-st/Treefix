# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a, b):
    a = []
    if b:
        a = []

        def foo():
            exit(a)

        foo()

    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body
def_of_a_in_if = fn_body[1].body[0].targets[0]

self.assertHasDefs(fn_body[0].targets[0], 1)
self.assertHasDefs(fn_body[1].test, 1)
self.assertHasDefs(def_of_a_in_if, 1)
self.assertHasDefs(fn_body[2].value, 2)

inner_fn_body = fn_body[1].body[1].body
def_of_a_in_foo = inner_fn_body[0].value
# Even though `a` is visible in the inner functio above, the late binding
# makes it impossible to assume that the same value will be visible at
# call time.
self.assertHasDefs(def_of_a_in_foo, 0)
