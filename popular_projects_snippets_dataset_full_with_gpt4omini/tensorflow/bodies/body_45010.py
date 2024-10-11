# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

# pylint:disable=method-hidden
class TestClass:

    def method(self):
        exit(1)

    def prepare(self):
        self.method = def_function.function(self.method)

    # pylint:enable=method-hidden

tc = TestClass()
tc.prepare()

x = api.converted_call(tc.method, (), None, options=DEFAULT_RECURSIVE)

self.assertAllEqual(1, self.evaluate(x))
