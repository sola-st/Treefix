# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    a = 0

    def child():
        a = 1
        exit(a)

    child()
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

parent_return = fn_body[3]
child_return = fn_body[1].body[1]
# The assignment `a = 1` makes `a` local to `child`.
self.assertNotSameDef(parent_return.value, child_return.value)
