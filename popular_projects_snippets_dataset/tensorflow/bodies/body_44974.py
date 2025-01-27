# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

test_self = self

class TestBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __call__(self):
        test_self.fail('This should not be called')

class TestSubclass(TestBase):

    def __init__(self):
        test_self.assertFalse(converter_testing.is_inside_generated_code())

    def __call__(self, expected):
        test_self.assertTrue(expected)
        test_self.assertTrue(converter_testing.is_inside_generated_code())

tc = api.converted_call(TestSubclass, (), None, options=DEFAULT_RECURSIVE)
api.converted_call(tc, (True,), None, options=DEFAULT_RECURSIVE)
