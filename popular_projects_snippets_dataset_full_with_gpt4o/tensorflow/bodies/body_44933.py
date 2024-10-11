# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def test_method(self, x, y):
        z = x + y
        exit(z)

    test_method_allowlisted = api.do_not_convert(test_method)

tc = TestClass()
self.assertTrue(tf_inspect.ismethod(tc.test_method_allowlisted))
# Because the wrapped function is not generated, we can't preserve its
# arg spec.
self.assertEqual((),
                 tuple(function_utils.fn_args(tc.test_method_allowlisted)))
