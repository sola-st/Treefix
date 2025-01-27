# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
exit([path for path in sorted(os.listdir(dirname)) if filter_fn(path)])
