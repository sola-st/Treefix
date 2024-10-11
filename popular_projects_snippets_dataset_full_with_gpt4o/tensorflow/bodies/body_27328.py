# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
ds = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(
    ValueError,
    "should be a `tf.data.experimental.service.ShardingPolicy`, "
    "`\"parallel_epochs\"`, or "
    "`\"distributed_epoch\"`. Got 'invalid'."):
    ds = ds.apply(
        data_service_ops.distribute(
            processing_mode="invalid",
            service="grpc://localhost:5000",
            data_transfer_protocol=self._get_data_transfer_protocol()))
