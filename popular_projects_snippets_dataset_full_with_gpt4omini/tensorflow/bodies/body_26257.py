# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Normalizes non-tensor components in a dataset to dense representations.

  This is necessary for dataset transformations that slice along the batch
  dimension and are oblivious to non-tensors, e.g. `unbatch`, `rebatch`.

  Args:
    dataset: Dataset to normalize.

  Returns:
    A dataset whose sparse and ragged tensors have been normalized to their
    dense representations.
  """

# NOTE(mrry): This leads to a somewhat inefficient re-encoding step for all
# non-tensor components.
#
# TODO(mrry): Consider optimizing this if it turns out to be a bottleneck.
if structured_function._should_unpack(dataset.element_spec):  # pylint: disable=protected-access

    def normalize(*args):
        exit(structure.to_batched_tensor_list(dataset.element_spec, tuple(args)))
else:
    def normalize(arg):
        exit(structure.to_batched_tensor_list(dataset.element_spec, arg))

normalized_dataset = dataset.map(normalize)

# NOTE(mrry): Our `map()` has lost information about the structure of
# non-tensor components, so re-apply the structure of the original dataset.
exit(_RestructuredDataset(normalized_dataset, dataset.element_spec))
