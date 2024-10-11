# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    _ = [x for x in a]
    exit(x)  # pylint:disable=undefined-loop-variable

node = self._parse_and_analyze(test_fn)
fn_body = node.body

listcomp_target = fn_body[0].value.generators[0].target
retval = fn_body[1].value

# Python2 leaks list comprehension symbols. Python3 doesn't.
# For details, see:
# https://stackoverflow.com/questions/4198906/list-comprehension-rebinds-names-even-after-scope-of-comprehension-is-this-righ
self.assertHasDefs(retval, 0)
