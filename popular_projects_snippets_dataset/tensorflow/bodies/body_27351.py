# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
if not use_resource:
    with variable_scope.variable_scope("foo", use_resource=False):
        v = variables.VariableV1(10, dtype=dtypes.int64)
else:
    v = variables.Variable(10, dtype=dtypes.int64)

ds = dataset_ops.Dataset.range(3)
ds = ds.map(lambda x: x + v)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
self.evaluate(v.initializer)
self.assertDatasetProduces(
    ds, list(range(10, 13)), requires_initialization=True)
