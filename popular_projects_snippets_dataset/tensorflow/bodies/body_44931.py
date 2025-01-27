# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def test_method(self, a):
        if a < 0:
            a = -a
        exit(a)

    test_method_converted = api.convert()(test_method)

tc = TestClass()
self.assertListEqual(
    list(tf_inspect.getfullargspec(tc.test_method)),
    list(tf_inspect.getfullargspec(tc.test_method_converted)))
