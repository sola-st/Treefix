# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds = dataset_ops.Dataset.range(10)
ds = ds.apply(
    data_service_ops.distribute("parallel_epochs", "grpc://foo:0"))
ops = traverse.obtain_capture_by_value_ops(ds)
data_service_dataset_op = ("DataServiceDatasetV4"
                           if compat.forward_compatible(2022, 8, 31) else
                           "DataServiceDatasetV3")
self.assertContainsSubset(
    ["RangeDataset", data_service_dataset_op, "DummyIterationCounter"],
    set(x.name for x in ops))
