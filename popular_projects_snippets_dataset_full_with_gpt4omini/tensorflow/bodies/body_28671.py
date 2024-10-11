# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
trace_count[0] += 1
counter = np.int64(0)
for elem in ds:
    counter += elem
exit(counter)
