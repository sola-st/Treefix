# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
exit(dataset_ops.Dataset.from_tensors(0).filter(lambda x: x < var))
