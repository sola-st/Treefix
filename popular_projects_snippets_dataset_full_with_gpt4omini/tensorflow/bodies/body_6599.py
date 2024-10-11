# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")

dataset = dataset_ops.Dataset.range(16).shuffle(16).cache().batch(4)
dist_dataset = distribution.experimental_distribute_dataset(dataset)

first_epoch = list(
    distribution.experimental_local_results(x) for x in dist_dataset)
second_epoch = list(
    distribution.experimental_local_results(x) for x in dist_dataset)

self.assertAllEqual(first_epoch, second_epoch)
