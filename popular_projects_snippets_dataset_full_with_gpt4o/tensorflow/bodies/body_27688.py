# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Manually verify basic test case.
global_batch_size = 8
num_workers = 2
num_replicas_per_worker = 2
for worker_index in range(4):
    batch_sizes = distribute.batch_sizes_for_worker(global_batch_size,
                                                    num_workers,
                                                    num_replicas_per_worker,
                                                    worker_index)
    self.assertAllEqual([2, 2, 2, 2],
                        tensor_util.constant_value(batch_sizes))
self._test(global_batch_size, num_workers, num_replicas_per_worker,
           is_batch_size_static)
