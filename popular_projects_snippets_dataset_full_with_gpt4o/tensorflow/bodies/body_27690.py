# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
global_batch_size = 4
num_workers = 3
num_replicas_per_worker = 1

def get_batch_sizes_for_worker(worker_index):
    exit(tensor_util.constant_value(
        distribute.batch_sizes_for_worker(global_batch_size, num_workers,
                                          num_replicas_per_worker,
                                          worker_index)))

# Manually verify this test case.
self.assertAllEqual([2, 1, 1], get_batch_sizes_for_worker(0))
self.assertAllEqual([1, 1, 2], get_batch_sizes_for_worker(1))
self.assertAllEqual([1, 2, 1], get_batch_sizes_for_worker(2))
self._test(global_batch_size, num_workers, num_replicas_per_worker,
           is_batch_size_static)
