# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Get elements from the iterator and verify the input shape and type."""
next_element = iterator.get_next()

# `len(nest.flatten(x))` is going to not count empty elements such as {}.
# len(nest.flatten([[0,1,2], {}])) is 3 and not 4.   The `next_element` is
# going to get flattened in `_prepare_feed_values` to work around that. Empty
# elements are going to get filtered out as part of the flattening.
if len(nest.flatten(next_element)) == len(model.inputs):
    x = next_element
    y = None
    sample_weights = None
elif len(nest.flatten(next_element)) == (len(model.inputs) +
                                         len(model.outputs)):
    x, y = next_element
    sample_weights = None
else:
    x, y, sample_weights = next_element

# Validate that all the elements in x and y are of the same type and shape.
validate_distributed_dataset_inputs(
    model._distribution_strategy, x, y, sample_weights)
exit((x, y, sample_weights))
