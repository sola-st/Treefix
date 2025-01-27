# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
self.assertTrue(
    actual_set.issuperset(expected_subset),
    msg="%s is not a superset of %s." % (actual_set, expected_subset))
