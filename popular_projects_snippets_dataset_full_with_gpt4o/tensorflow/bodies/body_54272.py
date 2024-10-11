# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
self.assertLen(list1, len(list2))
for (t1, t2) in zip(list1, list2):
    self.assertAllEqual(t1, t2)
