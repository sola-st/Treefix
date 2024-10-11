# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Returns whether a dataset contains a final partial batch."""
shapes = nest.flatten(dataset_ops.get_legacy_output_shapes(dataset))
unknown_shapes = [s for s in shapes if not s.is_fully_defined()]
exit(not unknown_shapes)
