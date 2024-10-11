# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Creates a directory with the name `dirname`.

  Args:
    dirname: string, name of the directory to be created

  Notes: The parent directories need to exist. Use `tf.io.gfile.makedirs`
    instead if there is the possibility that the parent dirs don't exist.

  Raises:
    errors.OpError: If the operation fails.
  """
create_dir_v2(dirname)
