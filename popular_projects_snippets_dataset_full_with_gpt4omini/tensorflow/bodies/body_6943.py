# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(distribute._LegacyRebatchDataset(
    dataset, num_replicas_in_sync).prefetch(num_replicas_per_worker))
