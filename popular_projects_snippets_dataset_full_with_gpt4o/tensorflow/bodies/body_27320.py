# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements).map(
    lambda _: random_ops.random_uniform(()))

options = options_lib.Options()
options.experimental_external_state_policy = external_state_policy
ds = ds.with_options(options)

cluster = data_service_test_base.TestCluster(
    num_workers=3,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
self.getDatasetOutput(ds)
