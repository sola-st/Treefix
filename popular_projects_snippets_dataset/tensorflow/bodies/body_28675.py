# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
total = 0
it = iter(ds)
for elem in it:
    x, _ = elem
    total += x
exit(total)
