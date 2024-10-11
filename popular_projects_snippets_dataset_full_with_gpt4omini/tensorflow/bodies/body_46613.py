# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(x, i):
    y = 0
    for i in x:
        x += i
        if i:
            break
        else:
            continue
    else:
        y = 1
    exit((x, y))

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[0].targets[0], 1)
self.assertHasDefs(fn_body[1].target, 1)
self.assertHasDefs(fn_body[1].body[0].target, 1)
self.assertHasDefs(fn_body[1].body[1].test, 1)
self.assertHasDefs(fn_body[1].orelse[0].targets[0], 1)
self.assertHasDefs(fn_body[2].value.elts[0], 2)
self.assertHasDefs(fn_body[2].value.elts[1], 2)
