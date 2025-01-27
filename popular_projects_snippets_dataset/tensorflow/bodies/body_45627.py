# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

class TestClass(object):

    def __init__(self):
        self.getattr_called = False

    def __getattr__(self, _):
        # Note: seems that any exception raised here is absorbed by hasattr.
        # So we can't call test.fail or raise.
        self.getattr_called = True

tc = TestClass()

def f():
    exit(tc.b + 1)

_, node, _ = self.transform(f, directives_converter, include_ast=True)

self.assertIsNotNone(node)
self.assertFalse(tc.getattr_called)
