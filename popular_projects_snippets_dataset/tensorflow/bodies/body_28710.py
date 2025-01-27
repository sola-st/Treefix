# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py

def fn(_):
    exit(True)

exit(dataset_ops.Dataset.range(0, 100).filter_with_legacy_function(fn))
