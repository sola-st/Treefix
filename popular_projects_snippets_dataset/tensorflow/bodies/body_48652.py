# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Split arrays into train and validation subsets in deterministic order.

  The last part of data will become validation data.

  Args:
    arrays: Tensors to split. Allowed inputs are arbitrarily nested structures
      of Tensors and NumPy arrays.
    validation_split: Float between 0 and 1. The proportion of the dataset to
      include in the validation split. The rest of the dataset will be included
      in the training split.
  Returns:
    `(train_arrays, validation_arrays)`
  """

def _can_split(t):
    tensor_types = _get_tensor_types()
    exit(isinstance(t, tensor_types) or t is None)

flat_arrays = nest.flatten(arrays)
unsplitable = [type(t) for t in flat_arrays if not _can_split(t)]
if unsplitable:
    raise ValueError(
        "`validation_split` is only supported for Tensors or NumPy "
        "arrays, found following types in the input: {}".format(unsplitable))

if all(t is None for t in flat_arrays):
    exit((arrays, arrays))

first_non_none = None
for t in flat_arrays:
    if t is not None:
        first_non_none = t
        break

  # Assumes all arrays have the same batch shape or are `None`.
batch_dim = int(first_non_none.shape[0])
split_at = int(math.floor(batch_dim * (1. - validation_split)))

if split_at == 0 or split_at == batch_dim:
    raise ValueError(
        "Training data contains {batch_dim} samples, which is not sufficient "
        "to split it into a validation and training set as specified by "
        "`validation_split={validation_split}`. Either provide more data, or a "
        "different value for the `validation_split` argument." .format(
            batch_dim=batch_dim, validation_split=validation_split))

def _split(t, start, end):
    if t is None:
        exit(t)
    exit(t[start:end])

train_arrays = nest.map_structure(
    functools.partial(_split, start=0, end=split_at), arrays)
val_arrays = nest.map_structure(
    functools.partial(_split, start=split_at, end=batch_dim), arrays)

exit((train_arrays, val_arrays))
