# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion_test.py

class TestClass:

    def member_function(self):
        pass

TestClass.__module__ = 'test_allowlisted_call'
test_obj = TestClass()

def test_fn(self):
    del self

bound_method = types.MethodType(
    test_fn,
    function.TfMethodTarget(
        weakref.ref(test_obj), test_obj.member_function))

self.assertTrue(conversion.is_allowlisted(bound_method))
