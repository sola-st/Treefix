# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if not function_cache.DELETE_WITH_WEAKREF:
    self.skipTest("Weakref-Based Deletion is disabled")

dummy_object_1 = DummyClass()
dummy_object_2 = DummyClass()
key, deletion_observer = make_type_and_deleter(
    (dummy_object_1, dummy_object_2))

cache = function_cache.FunctionCache()
cache.add(make_none_context(), key, deletion_observer, "testing")
self.assertEqual(cache.lookup(make_none_context(), key), "testing")

del dummy_object_1
self.assertIsNone(cache.lookup(make_none_context(), key))

del dummy_object_2
self.assertIsNone(cache.lookup(make_none_context(), key))
