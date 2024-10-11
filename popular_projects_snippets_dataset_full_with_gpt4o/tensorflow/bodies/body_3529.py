# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
cache.clear()
for key in keys:
    cache.add(make_none_context(), *key, "testing")
cache.add(make_none_context(),
          make_single_param_type(MockSubtypeOf2(3)),
          trace_type.WeakrefDeletionObserver(), "testing")
