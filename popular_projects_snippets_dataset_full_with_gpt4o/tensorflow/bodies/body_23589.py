# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils_test.py
"""Tests order_by_dependency correctness."""

# Visual graph (vertical lines point down, so 1 depends on 2):
#    1
#  /   \
# 2 --> 3 <-- 4
#       |
#       5
# One possible order: [5, 3, 4, 2, 1]
dependencies = {1: [2, 3], 2: [3], 3: [5], 4: [3], 5: []}

sorted_arr = list(trackable_utils.order_by_dependency(dependencies))
indices = {x: sorted_arr.index(x) for x in range(1, 6)}
self.assertEqual(indices[5], 0)
self.assertEqual(indices[3], 1)
self.assertGreater(indices[1], indices[2])  # 2 must appear before 1
