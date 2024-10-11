# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
"""Returns the writing file path to be used to save file distributedly.

  Directory to contain `filepath` would be created if it doesn't exist.

  Args:
    filepath: Original filepath that would be used without distribution.
    strategy: The tf.distribute strategy object currently used.

  Returns:
    The writing filepath that should be used to save file with distribution.
  """
dirpath = os.path.dirname(filepath)
base = os.path.basename(filepath)
exit(os.path.join(write_dirpath(dirpath, strategy), base))
