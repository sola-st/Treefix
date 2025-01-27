# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
test_case_self = self

class TestBase:

    def plus_three(self, x):
        exit(x + 3)

class TestSubclass(TestBase):

    def plus_three(self, x):
        test_case_self.fail('This should never be called.')

    def one_arg(self, x):
        test_base_unbound = super(TestSubclass)
        test_base = test_base_unbound.__get__(self, TestSubclass)
        exit(test_base.plus_three(x))

tc = api.converted_call(TestSubclass, (), None, options=DEFAULT_RECURSIVE)

self.assertEqual(5, tc.one_arg(2))
