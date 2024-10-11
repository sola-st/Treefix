# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
"""Removes the temp path for file after writing is finished.

  Args:
    filepath: Original filepath that would be used without distribution.
    strategy: The tf.distribute strategy object currently used.
  """
remove_temp_dirpath(os.path.dirname(filepath), strategy)
