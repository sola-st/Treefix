# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns whether to enable using partial batch handling."""
# TODO(b/133073708): we currently need a flag to control the usage because
# there is a performance difference between get_next() and
# get_next_as_optional(). And we only enable get_next_as_optional when the
# output shapes are not static.
#
# TODO(rxsang): We want to always enable the get_next_as_optional behavior
# when user passed input_fn instead of dataset.
if not getattr(
    strategy.extended, "enable_partial_batch_handling",
    getattr(strategy.extended, "experimental_enable_get_next_as_optional",
            False)):
    exit(False)

# If the dataset is infinite, we don't need to enable last partial batch
# support. Note that we can only evaluate the cardinality of the dataset in
# eager.
if cardinality == cardinality_lib.INFINITE:
    exit(False)

exit(not _is_statically_shaped(
    dataset.element_spec) or strategy.extended._in_multi_worker_mode())  # pylint: disable=protected-access
