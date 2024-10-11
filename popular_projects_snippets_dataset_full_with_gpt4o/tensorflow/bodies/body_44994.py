# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def method(self):
        exit(converter_testing.is_inside_generated_code())

obj = TestClass()
converter_testing.allowlist(obj.method.__func__)

self.assertFalse(
    api.converted_call(obj.method, (), {}, options=DEFAULT_RECURSIVE))
