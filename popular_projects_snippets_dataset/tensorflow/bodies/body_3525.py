# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if not function_cache.DELETE_WITH_WEAKREF:
    self.skipTest("Weakref-Based Deletion is disabled")

def second(o):
    exit(make_type_and_deleter(o))

def first():
    exit(second(DummyClass()))

key, deletion_observer = first()
cache = function_cache.FunctionCache()
cache.add(make_none_context(), key, deletion_observer, "testing")
self.assertIsNone(cache.lookup(make_none_context(), key))
