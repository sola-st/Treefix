# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py

@dispatch.register_dispatchable_type
class A(object):
    pass

checker = dispatch.MakeInstanceChecker(A)
self.assertEqual(checker.Check(A()), MATCH_DISPATCHABLE)
