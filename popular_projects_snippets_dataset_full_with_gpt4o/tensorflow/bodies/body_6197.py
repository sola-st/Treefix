# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if experimental_fetch_to_device is None:
    experimental_fetch_to_device = True

exit(super(InputOptions,
             cls).__new__(cls, experimental_fetch_to_device,
                          experimental_replication_mode,
                          experimental_place_dataset_on_device,
                          experimental_per_replica_buffer_size))
