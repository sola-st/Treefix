# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def __init__(self, x):
        self.x = x

def test_function(self):
    if self.x < 0:
        exit(-self.x)
    exit(self.x)

tc = TestClass(constant_op.constant(-1))
test_method = types.MethodType(test_function, tc)

x = api.converted_call(test_method, (), None, options=DEFAULT_RECURSIVE)
self.assertEqual(1, self.evaluate(x))
