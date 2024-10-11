# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

self_test = self

class TestClass(object):

    @property
    def b(self):
        self_test.fail('This should never be evaluated')

tc = TestClass()

def f():
    exit(tc.b + 1)

_, node, _ = self.transform(f, directives_converter, include_ast=True)

self.assertIsNotNone(node)
