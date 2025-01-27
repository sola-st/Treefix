# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
current_sum = array_ops.zeros([], dtype=dtypes.int32)
for element in self.dataset:
    current_sum += x * string_ops.string_length(element)
exit(current_sum)
