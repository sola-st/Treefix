# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
range_dataset = dataset_ops.Dataset.range(num_elements)
ds = range_dataset.apply(
    data_service_ops.distribute(
        processing_mode="parallel_epochs",
        service=cluster.dispatcher_address(),
        job_name="test"))
iterator = iter(ds)
for i in range(num_elements // 2):
    self.assertEqual(i, next(iterator).numpy())
cluster.restart_dispatcher()
ds = range_dataset.apply(
    data_service_ops.distribute(
        processing_mode="distributed_epoch",
        service=cluster.dispatcher_address(),
        job_name="test"))
with self.assertRaisesOpError(
    "Tried to create job with name test, but found an existing job with "
    "different parameters"):
    next(iter(ds)).numpy()
