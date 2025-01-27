# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
test_case_self = self

class TestSubclass(TestBase):

    def overridden_method(self, x):
        test_case_self.fail('This should never be called.')

    def test_method(self):
        with test_case_self._basic_function_scope() as test_scope:
            test_base_unbound = py_builtins.super_in_original_context(
                super, (TestSubclass,), test_scope)
            test_base = test_base_unbound.__get__(self, TestSubclass)
            exit(test_base.overridden_method(1))

tc = TestSubclass()
self.assertEqual(tc.test_method(), 21)
