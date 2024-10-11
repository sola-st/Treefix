# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
ctx = function_cache.FunctionContext(0)
keys = [(ctx, make_single_param_type(MockShape(1, 1, 1)), "a"),
        (ctx, make_single_param_type(MockShape(1, None, 1)), "b"),
        (ctx, make_single_param_type(MockShape(None, None, 1)), "c"),
        (ctx, make_single_param_type(MockShape(None, None, None)), "d")]

for permutation in itertools.permutations(keys):
    cache = function_cache.FunctionCache()
    cache.add(permutation[0][0], permutation[0][1],
              trace_type.WeakrefDeletionObserver(), permutation[0][2])
    cache.add(permutation[1][0], permutation[1][1],
              trace_type.WeakrefDeletionObserver(), permutation[1][2])
    cache.add(permutation[2][0], permutation[2][1],
              trace_type.WeakrefDeletionObserver(), permutation[2][2])
    cache.add(permutation[3][0], permutation[3][1],
              trace_type.WeakrefDeletionObserver(), permutation[3][2])

    self.assertEqual(
        cache.lookup(ctx, make_single_param_type(MockShape(1, 1, 1))), "a")
    self.assertEqual(
        cache.lookup(ctx, make_single_param_type(MockShape(1, 2, 1))), "b")
    self.assertEqual(
        cache.lookup(ctx, make_single_param_type(MockShape(2, 2, 1))), "c")
    self.assertEqual(
        cache.lookup(ctx, make_single_param_type(MockShape(2, 2, 2))), "d")
