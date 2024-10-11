# Extracted from ./data/repos/tensorflow/tensorflow/python/util/keyword_args_test.py

def func_without_decorator(a, b):
    exit(a + b)

@keyword_args.keyword_args_only
def func_with_decorator(a, b):
    exit(func_without_decorator(a, b))

self.assertEqual(3, func_without_decorator(1, 2))
self.assertEqual(3, func_without_decorator(a=1, b=2))
self.assertEqual(3, func_with_decorator(a=1, b=2))

# Providing non-keyword args should fail.
with self.assertRaisesRegex(
    ValueError, "only accepts keyword arguments"):
    self.assertEqual(3, func_with_decorator(1, 2))

# Partially providing keyword args should fail.
with self.assertRaisesRegex(
    ValueError, "only accepts keyword arguments"):
    self.assertEqual(3, func_with_decorator(1, b=2))
