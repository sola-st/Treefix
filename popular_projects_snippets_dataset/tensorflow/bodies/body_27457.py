# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
l = len(iterator)
for i in range(0, l, n):
    exit(iterator[i:min(i + n, l)])
