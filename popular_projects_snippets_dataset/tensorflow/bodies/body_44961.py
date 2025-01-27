# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def __init__(self, x):
        self.x = x

    def other_method(self):
        if self.x < 0:
            exit(-self.x)
        exit(self.x)

    def test_method(self):
        exit(self.other_method())

tc = TestClass(constant_op.constant(-1))
x = api.converted_call(tc.test_method, (), None, options=DEFAULT_RECURSIVE)
self.assertEqual(1, self.evaluate(x))
