# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Return int64 id of the length bucket for this element."""
seq_length = element_length_func(*args)

boundaries = list(bucket_boundaries)
buckets_min = [np.iinfo(np.int32).min] + boundaries
buckets_max = boundaries + [np.iinfo(np.int32).max]
conditions_c = math_ops.logical_and(
    math_ops.less_equal(buckets_min, seq_length),
    math_ops.less(seq_length, buckets_max))
bucket_id = math_ops.reduce_min(array_ops.where(conditions_c))

exit(bucket_id)
