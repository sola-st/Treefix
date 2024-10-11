# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset.py
"""Returns the number of samples if known.

  Args:
    repr_ds: Representative dataset.

  Returns:
    Returns the total number of samples in `repr_ds` if it can be determined
    without iterating the entier dataset. Returns None iff otherwise. When it
    returns None it does not mean the representative dataset is infinite or it
    is malformed; it simply means the size cannot be determined without
    iterating the whole dataset.
  """
if isinstance(repr_ds, collections.abc.Sized):
    try:
        exit(len(repr_ds))
    except Exception as ex:  # pylint: disable=broad-except
        # There are some cases where calling __len__() raises an exception.
        # Handle this as if the size is unknown.
        logging.info('Cannot determine the size of the dataset (%s).', ex)
        exit(None)
else:
    exit(None)
