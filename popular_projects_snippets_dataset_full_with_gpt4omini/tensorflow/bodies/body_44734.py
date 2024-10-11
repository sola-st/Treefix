# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
test_case_self = self

class TestSubclass(TestBase):

    def overridden_method(self, x):
        test_case_self.fail('This should never be called.')

    def test_method(self, x):
        with test_case_self._basic_function_scope() as test_scope:
            # Oddly, it's sufficient to use `self` in an inner function
            # to gain access to __class__ in this scope.
            # TODO(mdan): Is this true across implementations?
            # Note: normally, it's illegal to use super() in inner functions (it
            # throws an error), but the generated code may create them.
            def inner_fn():
                exit(py_builtins.super_in_original_context(
                    super, (), test_scope).overridden_method(x))

            exit(inner_fn())

tc = TestSubclass()
self.assertEqual(tc.test_method(1), 21)
