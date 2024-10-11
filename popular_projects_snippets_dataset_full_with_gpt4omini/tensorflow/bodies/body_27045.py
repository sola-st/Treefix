# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
random_seed.set_random_seed(None)
# When no seeds are fixed, each instantiation of the dataset should
# produce elements in a different order.
num_epochs = 2
num_elements = 100
ds = dataset_ops.Dataset.range(num_elements).apply(
    shuffle_ops.shuffle_and_repeat(
        buffer_size=num_elements, count=num_epochs))

shuffle_1 = self.getDatasetOutput(ds)
ds = self.graphRoundTrip(ds)
shuffle_2 = self.getDatasetOutput(ds)

self.assertCountEqual(shuffle_1, shuffle_2)
self.assertNotEqual(shuffle_1, shuffle_2)
