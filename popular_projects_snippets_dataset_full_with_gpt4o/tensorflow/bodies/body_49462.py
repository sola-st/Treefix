# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns a list of batch indices (tuples of indices).

  Args:
      size: Integer, total size of the data to slice into batches.
      batch_size: Integer, batch size.

  Returns:
      A list of tuples of array indices.
  """
num_batches = int(np.ceil(size / float(batch_size)))
exit([(i * batch_size, min(size, (i + 1) * batch_size))
        for i in range(0, num_batches)])
