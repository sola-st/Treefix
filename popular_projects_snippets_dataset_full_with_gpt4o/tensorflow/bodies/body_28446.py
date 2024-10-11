# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
dataset = dataset_ops.Dataset.range(5)
dataset = dataset.apply(testing.assert_next(["MapAndBatch"]))
dataset = dataset.map(lambda x: x * 2).batch(5)
self.evaluate(dataset.reduce(0, lambda state, value: state))
