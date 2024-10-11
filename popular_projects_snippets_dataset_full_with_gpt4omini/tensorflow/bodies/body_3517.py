# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
cache = function_cache.FunctionCache()
f_type_1, deletion_observer_1 = make_type_and_deleter(1)
cache.add(make_none_context(), f_type_1, deletion_observer_1, "test_1")
self.assertEqual(
    cache.lookup(make_none_context(), f_type_1), "test_1")
cache.delete(make_none_context(), f_type_1)
self.assertIsNone(cache.lookup(make_none_context(), f_type_1))

f_type_2 = make_single_param_type(MockSubtypeOf2(2))
cache.add(make_none_context(), f_type_2,
          trace_type.WeakrefDeletionObserver(), "test_2")
self.assertEqual(
    cache.lookup(make_none_context(), f_type_2), "test_2")

f_type_3 = make_single_param_type(MockSubtypeOf2(3))
self.assertEqual(
    cache.lookup(make_none_context(), f_type_3), "test_2")

cache.delete(make_none_context(), f_type_2)
self.assertIsNone(cache.lookup(make_none_context(), f_type_2))
self.assertIsNone(cache.lookup(make_none_context(), f_type_3))
