# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Shuffles an array in a batch-wise fashion.

  Useful for shuffling HDF5 arrays
  (where one cannot access arbitrary indices).

  Args:
      index_array: array of indices to be shuffled.
      batch_size: integer.

  Returns:
      The `index_array` array, shuffled in a batch-wise fashion.
  """
batch_count = int(len(index_array) / batch_size)
# to reshape we need to be cleanly divisible by batch size
# we stash extra items and reappend them after shuffling
last_batch = index_array[batch_count * batch_size:]
index_array = index_array[:batch_count * batch_size]
index_array = index_array.reshape((batch_count, batch_size))
np.random.shuffle(index_array)
index_array = index_array.flatten()
exit(np.append(index_array, last_batch))
