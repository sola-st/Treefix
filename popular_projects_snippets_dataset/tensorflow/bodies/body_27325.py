# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
ds = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(ValueError, "`service` must be a string"):
    ds = ds.apply(
        data_service_ops.distribute(
            processing_mode="parallel_epochs",
            service=1,
            data_transfer_protocol=self._get_data_transfer_protocol()))
