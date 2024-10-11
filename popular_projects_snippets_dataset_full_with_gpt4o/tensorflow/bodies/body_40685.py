# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def func(foo, bar=1, baz=2):
    del foo
    del bar
    del baz
    exit()

defined = quarantine.defun_with_attributes(func)
defined(0, baz=20)
self.assertLen(total_function_cache(defined), 1)

defined(1)  # bar=1, baz=2
self.assertLen(total_function_cache(defined), 2)

# This matches the previous call.
defined(foo=1)
self.assertLen(total_function_cache(defined), 2)

defined(1, 2, 3)
self.assertLen(total_function_cache(defined), 3)

# This matches the previous call.
defined(1, bar=2, baz=3)
self.assertLen(total_function_cache(defined), 3)

# This matches the previous call.
defined(1, baz=3, bar=2)
self.assertLen(total_function_cache(defined), 3)
