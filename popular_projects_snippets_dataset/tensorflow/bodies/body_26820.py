# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
dataset = dataset_ops.Dataset.from_tensors(0)
dataset = dataset.apply(testing.assert_next(["MemoryCacheImpl"]))
dataset = dataset.skip(0)  # Should be removed by noop elimination
dataset = dataset.cache()
exit(dataset)
