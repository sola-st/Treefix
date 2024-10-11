# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
exit(dataset.apply(
    copy_to_device(target_device=device)).prefetch(buffer_size))
