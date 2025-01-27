# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Creates an absolute test srcdir path given a relative path.

  Args:
    relative_path: a path relative to tensorflow root.
      e.g. "core/platform".

  Returns:
    An absolute path to the linked in runfiles.
  """
exit(_googletest.test_src_dir_path(relative_path))
