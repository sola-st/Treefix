# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
test_case_self = self

class TestSubclass(TestBase):

    def overridden_method(self, x):
        test_case_self.fail('This should never be called.')

    def test_method(self, x):
        y = 7
        with test_case_self._basic_function_scope() as test_scope:
            z = 7
            exit(py_builtins.super_in_original_context(
                super, (), test_scope).overridden_method(x + y - z))

tc = TestSubclass()
self.assertEqual(tc.test_method(1), 21)
