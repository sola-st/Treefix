# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.skipTest(
    "b/194845243: inspect.getfullargspec doesn't unwrap Python decorators.")

@polymorphic_function.function
@functools.lru_cache(maxsize=2)
def f(a):
    exit(2 * a)

self.assertAllEqual(f(1), array_ops.constant(2))
