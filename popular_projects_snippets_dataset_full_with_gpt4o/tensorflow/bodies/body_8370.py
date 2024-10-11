# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Use all_gather_fn to aggregate `IndexedSlices`."""
all_values = all_gather_fn(input_slices.values, options)
# Add control dependency to order the all-gather.
if (options.implementation ==
    collective_util.CommunicationImplementation.NCCL):
    control = [all_values]
else:
    control = []
with ops.control_dependencies(control):
    all_indices = all_gather_fn(input_slices.indices, options)
exit(indexed_slices.IndexedSlices(
    values=all_values,
    indices=all_indices,
    dense_shape=input_slices.dense_shape))
