# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
dataset = dataset_ops.Dataset.from_tensors(0)
dataset = dataset.apply(testing.assert_next(["MapAndBatch"]))
# Should be fused by map and batch fusion
dataset = dataset.map(lambda x: x)
dataset = dataset.batch(1)
exit(dataset)
