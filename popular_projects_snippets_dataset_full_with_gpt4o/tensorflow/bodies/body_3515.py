# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
cache = function_cache.FunctionCache()

f_type_1, deletion_observer_1 = make_type_and_deleter(1)
self.assertIsNone(cache.lookup(make_none_context(), f_type_1))

f_type_2, deletion_observer_2 = make_type_and_deleter(2)
f_type_3, _ = make_type_and_deleter(3)

cache.add(make_none_context(), f_type_1, deletion_observer_1, "test_1")
cache.add(make_none_context(), f_type_2, deletion_observer_2, "test_2")

self.assertEqual(
    cache.lookup(make_none_context(), f_type_1), "test_1")
self.assertEqual(
    cache.lookup(make_none_context(), f_type_2), "test_2")
self.assertIsNone(cache.lookup(make_none_context(), f_type_3))
