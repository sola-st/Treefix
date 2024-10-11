# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
self._test(
    global_batch_size=4,
    num_workers=5,
    num_replicas_per_worker=1,
    is_batch_size_static=is_batch_size_static)
