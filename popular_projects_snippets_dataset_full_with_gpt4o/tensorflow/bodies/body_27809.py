# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
trace_count[0] += 1
counter = np.int64(0)
for _ in range(5):
    elem = next(iterator)
    counter += elem[0]
    counter += elem[1]
exit(counter)
