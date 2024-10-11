# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

tested_codepaths = set()
def some_function_with_forward_compat_behavior():
    if compat.forward_compatible(2050, 1, 1):
        tested_codepaths.add("future")
    else:
        tested_codepaths.add("present")

@test_util.with_forward_compatibility_horizons(None, [2051, 1, 1])
def some_test(self):
    del self  # unused
    some_function_with_forward_compat_behavior()

some_test(None)
self.assertEqual(tested_codepaths, set(["present", "future"]))
