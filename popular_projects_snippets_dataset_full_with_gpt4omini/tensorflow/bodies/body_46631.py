# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def foo(a):
    exit(a)

def test_fn(a):
    a = foo(a)
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

param = node.args.args[0]
source = fn_body[0].value.args[0]
target = fn_body[0].targets[0]
retval = fn_body[1].value
self.assertSameDef(param, source)
self.assertNotSameDef(source, target)
self.assertSameDef(target, retval)
