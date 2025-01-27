# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
sum_keywords = 0
for i in range(num_files):
    for j in range(self._num_records):
        sum_keywords += 1 + (i + j) % 2
exit(sum_keywords)
