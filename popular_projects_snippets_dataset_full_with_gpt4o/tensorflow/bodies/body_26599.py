# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/snapshot.py
exit(_LegacySnapshotDataset(
    input_dataset=dataset,
    path=path,
    compression=compression,
    reader_path_prefix=reader_path_prefix,
    writer_path_prefix=writer_path_prefix,
    shard_size_bytes=shard_size_bytes,
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds,
    num_reader_threads=num_reader_threads,
    reader_buffer_size=reader_buffer_size,
    num_writer_threads=num_writer_threads,
    writer_buffer_size=writer_buffer_size,
    shuffle_on_read=shuffle_on_read,
    shuffle_seed=shuffle_seed,
    mode=mode,
    snapshot_name=snapshot_name))
