# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors(range(4))
options = options_lib.Options()
options.experimental_optimization.map_and_batch_fusion = True
dataset = dataset.with_options(options)

self.assertAllEqual(self.evaluate(random_access.at(dataset, 0)), range(4))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 1))
