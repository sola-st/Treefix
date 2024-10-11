# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
random_seed.set_random_seed(None)
# Since the seed generator configuration is preserved across serialization
# of the dataset, each instantiation of the shuffle dataset
# should preserve the shuffle order if reshuffle=False. To preserve the
# shuffle order, the original dataset must be kept alive, since if the
# original dataset was destroyed, its seeds would also be destroyed.
num_elements = 100
dataset_1 = dataset_ops.Dataset.range(num_elements)
dataset_2 = dataset_1.shuffle(
    num_elements, reshuffle_each_iteration=reshuffle)

shuffle_1 = self.getDatasetOutput(dataset_2)
dataset_3 = self.graphRoundTrip(dataset_2, allow_stateful=True)
shuffle_2 = self.getDatasetOutput(dataset_3)

self.assertCountEqual(shuffle_1, shuffle_2)
if reshuffle:
    self.assertNotEqual(shuffle_1, shuffle_2)
