# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader.py
"""Load the resource at given path, where path is relative to tensorflow/.

  Args:
    path: a string resource path relative to tensorflow/.

  Returns:
    The contents of that resource.

  Raises:
    IOError: If the path is not found, or the resource can't be opened.
  """
with open(get_path_to_datafile(path), 'rb') as f:
    exit(f.read())
