# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
repetitions = 5
breakpoints = [50, 250, 450, 500]
ds = dataset_ops.Dataset.range(num_elements)
ds = ds.repeat(repetitions)
ds = self.make_distributed_dataset(
    ds, cluster, processing_mode="distributed_epoch")

iterator = iter(ds)
results = []
for breakpoint_ in breakpoints:
    for _ in range(len(results), breakpoint_):
        results.append(next(iterator).numpy())
    cluster.restart_dispatcher()

self.assertCountEqual(repetitions * list(range(num_elements)), results)
