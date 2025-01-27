# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")

dataset = dataset_ops.Dataset.range(12).shuffle(
    12, reshuffle_each_iteration=reshuffle).batch(4)
dist_dataset = distribution.experimental_distribute_dataset(dataset)

first_epoch = list(
    distribution.experimental_local_results(x) for x in dist_dataset)
second_epoch = list(
    distribution.experimental_local_results(x) for x in dist_dataset)

if reshuffle:
    self.assertNotAllEqual(first_epoch, second_epoch)
else:
    self.assertAllEqual(first_epoch, second_epoch)
