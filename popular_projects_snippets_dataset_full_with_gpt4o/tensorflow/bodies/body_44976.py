# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

test_self = self

class TestClass:

    def __init__(self):
        test_self.assertFalse(converter_testing.is_inside_generated_code())

tc = api.converted_call(TestClass, (), None, options=DEFAULT_RECURSIVE)
self.assertIsInstance(tc, TestClass)
