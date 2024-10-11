# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
shapes = nest.flatten(dataset_ops.get_legacy_output_shapes(iterator))
# Take the batch size from the first element, as it should be the same for
# all.
dims = shapes[0].dims
exit(dims[0] if dims else None)
