# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion_test.py

allowlisted_mod = imp.new_module('test_allowlisted_call')
sys.modules['test_allowlisted_call'] = allowlisted_mod
config.CONVERSION_RULES = ((config.DoNotConvert('test_allowlisted_call'),) +
                           config.CONVERSION_RULES)

class TestClass:

    def __call__(self):
        pass

    def allowlisted_method(self):
        pass

TestClass.__module__ = 'test_allowlisted_call'
TestClass.__call__.__module__ = 'test_allowlisted_call'

class Subclass(TestClass):

    def converted_method(self):
        pass

tc = Subclass()

self.assertTrue(conversion.is_allowlisted(TestClass.__call__))
self.assertTrue(conversion.is_allowlisted(tc))
self.assertTrue(conversion.is_allowlisted(tc.__call__))
self.assertTrue(conversion.is_allowlisted(tc.allowlisted_method))
self.assertFalse(conversion.is_allowlisted(Subclass))
self.assertFalse(conversion.is_allowlisted(tc.converted_method))
