# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

self.assertEqual(
    inspect_utils.getmethodclass(free_function), None)
self.assertEqual(
    inspect_utils.getmethodclass(free_factory()), None)

self.assertEqual(
    inspect_utils.getmethodclass(TestClass.member_function),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(TestClass.decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(TestClass.fn_decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(TestClass.wrap_decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(TestClass.static_method),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(TestClass.class_method),
    TestClass)

test_obj = TestClass()
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.member_function),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.fn_decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.wrap_decorated_member),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.static_method),
    TestClass)
self.assertEqual(
    inspect_utils.getmethodclass(test_obj.class_method),
    TestClass)
