# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
exit(dataset_ops.Dataset.from_tensors(0).repeat().scan(
    initial_state=start, scan_func=scan_fn))
