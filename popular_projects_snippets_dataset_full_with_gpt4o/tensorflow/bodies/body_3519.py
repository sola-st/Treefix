# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
ctx = function_cache.FunctionContext(0)
cache = function_cache.FunctionCache()
cache.add(ctx, make_single_param_type(MockShape(1, 2, None)),
          trace_type.WeakrefDeletionObserver(), "a")
cache.add(ctx, make_single_param_type(MockShape(1, None, 3)),
          trace_type.WeakrefDeletionObserver(), "b")

self.assertEqual(
    cache.lookup(ctx, make_single_param_type(MockShape(1, 2, 3))),
    "a")
