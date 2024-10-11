# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
trace_count[0] += 1
counter = np.int64(0)
for _ in range(5):
    next(iterator)
    counter += 1
exit(counter)
