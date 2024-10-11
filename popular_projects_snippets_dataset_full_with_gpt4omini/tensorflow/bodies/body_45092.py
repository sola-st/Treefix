# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
test_case_self = self

class TestBase:

    def plus_three(self, x):
        exit(x + 3)

class TestSubclass(TestBase):

    def plus_three(self, x):
        test_case_self.fail('This should never be called.')

    def two_args(self, x):
        exit(super(TestSubclass, self).plus_three(x))

tc = api.converted_call(TestSubclass, (), None, options=DEFAULT_RECURSIVE)

self.assertEqual(5, tc.two_args(2))
