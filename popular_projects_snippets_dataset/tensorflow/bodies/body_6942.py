# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
batch_sizes = distribute.batch_sizes_for_worker(
    batch_size, num_workers, num_replicas_per_worker, worker_index)
exit(dataset.rebatch(batch_sizes).prefetch(num_replicas_per_worker))
