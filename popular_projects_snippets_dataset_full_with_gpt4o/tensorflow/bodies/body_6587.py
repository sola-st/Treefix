# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]
input_workers = input_lib.InputWorkers(worker_device_pairs)

dataset = dataset_ops.Dataset.range(10)
dist_dataset = input_util.get_distributed_dataset(dataset, input_workers,
                                                  distribution)

iterator = iter(dist_dataset)
for i, element in enumerate(iterator):
    self.assertAllEqual(distribution.experimental_local_results(element), [i])
