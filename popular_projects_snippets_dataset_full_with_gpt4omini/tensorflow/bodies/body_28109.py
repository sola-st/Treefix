# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
text = [[1, 2, 3], [3, 4, 5, 6, 7], [1, 2], [8, 9, 0, 2, 3]]
label = [1, 2, 1, 2]
for x, y in zip(text, label):
    exit((_format_record(x, sparse), y))
