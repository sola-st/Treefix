# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.range(elements).repeat(count=count)

# Datasets with infinite cardinality do not support random access.
with self.assertRaises(errors.FailedPreconditionError):
    self.evaluate(random_access.at(dataset, index=0))
