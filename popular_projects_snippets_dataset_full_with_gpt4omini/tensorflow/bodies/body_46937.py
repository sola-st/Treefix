# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

def local_function():
    pass

class LocalClass:

    def member_function(self):
        pass

    @decorator
    def decorated_member(self):
        pass

    @function_decorator()
    def fn_decorated_member(self):
        pass

    @wrapping_decorator()
    def wrap_decorated_member(self):
        pass

self.assertEqual(
    inspect_utils.getmethodclass(local_function), None)

self.assertEqual(
    inspect_utils.getmethodclass(LocalClass.member_function),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(LocalClass.decorated_member),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(LocalClass.fn_decorated_member),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(LocalClass.wrap_decorated_member),
    LocalClass)

test_obj = LocalClass()
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.member_function),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.decorated_member),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.fn_decorated_member),
    LocalClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.wrap_decorated_member),
    LocalClass)
