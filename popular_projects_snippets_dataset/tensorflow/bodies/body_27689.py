# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
exit(tensor_util.constant_value(
    distribute.batch_sizes_for_worker(global_batch_size, num_workers,
                                      num_replicas_per_worker,
                                      worker_index)))
