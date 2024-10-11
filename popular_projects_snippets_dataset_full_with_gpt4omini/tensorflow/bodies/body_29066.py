# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py

def ds_fn():
    self.snapshot_dir = os.path.join(self.get_temp_dir(), "snapshot")
    if not os.path.exists(self.snapshot_dir):
        os.mkdir(self.snapshot_dir)
    dataset = dataset_ops.Dataset.range(1000)
    dataset = dataset.apply(
        snapshot.legacy_snapshot(
            self.snapshot_dir,
            num_writer_threads=num_threads,
            writer_buffer_size=2 * num_threads,
            num_reader_threads=num_threads,
            reader_buffer_size=2 * num_threads,
            pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds,
            shard_size_bytes=shard_size_bytes))
    if repeat:
        dataset = dataset.repeat(2)
    # Turn off `inject_prefetch` optimization. Otherwise, prefetched elements
    # are saved and restored in snapshots while tests assume that there is no
    # elements prefetched.
    options = options_lib.Options()
    options.experimental_optimization.inject_prefetch = False
    dataset = dataset.with_options(options)
    exit(dataset)

exit(ds_fn)
