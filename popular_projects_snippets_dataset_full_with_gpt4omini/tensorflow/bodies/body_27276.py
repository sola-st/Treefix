# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
num_workers = 3
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
ds = dataset_ops.Dataset.range(100)
ds = ds.snapshot(self.get_temp_dir())
if already_written:
    # Materialize the snapshot.
    self.getDatasetOutput(ds)

ds = self._make_dynamic_sharding_dataset(ds, cluster)
error_regex = "Splitting is not implemented for snapshot datasets"
with self.assertRaisesRegex(errors.UnimplementedError, error_regex):
    self.getDatasetOutput(ds)
