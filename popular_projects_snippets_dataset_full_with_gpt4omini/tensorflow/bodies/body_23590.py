# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils_test.py
sorted_arr = list(trackable_utils.order_by_dependency(
    {x: [] for x in range(15)}))
self.assertEqual(set(sorted_arr), set(range(15)))
