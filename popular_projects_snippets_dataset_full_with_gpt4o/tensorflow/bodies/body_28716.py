# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py

def fn():
    exit(range(100))

exit(dataset_ops.Dataset.from_generator(fn, output_types=dtypes.float32))
