# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=3)
num_samples = 200
weights = [.6, .3, .1]
classes = len(weights)

# Create a dataset that samples each integer in `[0, num_datasets)`
# with probability given by `weights[i]`.
ds = dataset_ops.Dataset.sample_from_datasets(
    [dataset_ops.Dataset.from_tensors(i).repeat() for i in range(classes)],
    weights)
ds = self._make_dynamic_sharding_dataset(ds, cluster)
ds = ds.take(num_samples)

freqs = np.zeros([classes])
for v in self.getDatasetOutput(ds, requires_initialization=True):
    freqs[v] += 1

self.assertGreater(freqs[0], freqs[1])
self.assertGreater(freqs[1], freqs[2])
