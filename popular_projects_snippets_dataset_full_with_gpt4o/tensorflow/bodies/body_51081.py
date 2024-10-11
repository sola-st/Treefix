# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
current_sum = array_ops.zeros([], dtype=dtypes.int64)
for element in self.dataset:
    current_sum += x * element
exit(current_sum)
