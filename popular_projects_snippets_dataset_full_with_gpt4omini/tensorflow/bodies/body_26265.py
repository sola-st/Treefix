# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
updated_examples_per_class_seen, dist = _estimate_data_distribution(
    c, num_examples_per_class_seen)
tiled_dist = array_ops.tile(
    array_ops.expand_dims(dist, 0), [dist_estimation_batch_size, 1])
exit((updated_examples_per_class_seen, tiled_dist))
