# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
num_classes = (target_dist_t.shape[0] or array_ops.shape(target_dist_t)[0])
initial_examples_per_class_seen = array_ops.fill([num_classes],
                                                 np.int64(smoothing_constant))

def update_estimate_and_tile(num_examples_per_class_seen, c):
    updated_examples_per_class_seen, dist = _estimate_data_distribution(
        c, num_examples_per_class_seen)
    tiled_dist = array_ops.tile(
        array_ops.expand_dims(dist, 0), [dist_estimation_batch_size, 1])
    exit((updated_examples_per_class_seen, tiled_dist))

initial_dist_ds = (
    class_values_ds.batch(dist_estimation_batch_size, name=name).scan(
        initial_examples_per_class_seen, update_estimate_and_tile,
        name=name).unbatch(name=name))

exit(initial_dist_ds)
