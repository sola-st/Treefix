# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def foo(self):
        pass

tc = TestClass()

# `method.__get__()` returns a so-called method-wrapper.
wrapper = api.converted_call(
    tc.foo.__get__, (tc,), None, options=DEFAULT_RECURSIVE)
self.assertEqual(wrapper, tc.foo)
