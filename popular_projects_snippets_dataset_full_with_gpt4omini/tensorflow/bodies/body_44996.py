# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def method(self):
        exit(converter_testing.is_inside_generated_code())

converter_testing.allowlist(TestClass)

obj = TestClass()
self.assertFalse(
    api.converted_call(obj.method, (), {}, options=DEFAULT_RECURSIVE))
