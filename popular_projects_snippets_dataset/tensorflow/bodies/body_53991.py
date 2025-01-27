# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaises(AssertionError):
    self._WeMustGoDeeper("this_is_not_the_error_you_are_looking_for")

self._WeMustGoDeeper("true_err")
self._WeMustGoDeeper("name")
self._WeMustGoDeeper("orig")
