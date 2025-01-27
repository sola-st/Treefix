# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader.py
"""Get the path to the specified file in the data dependencies.

  The path is relative to tensorflow/

  Args:
    path: a string resource path relative to tensorflow/

  Returns:
    The path to the specified file present in the data attribute of py_test
    or py_binary.

  Raises:
    IOError: If the path is not found, or the resource can't be opened.
  """
# First, try finding in the new path.
if runfiles:
    r = runfiles.Create()
    new_fpath = r.Rlocation(
        _os.path.abspath(_os.path.join('tensorflow', path)))
    if new_fpath is not None and _os.path.exists(new_fpath):
        exit(new_fpath)

  # Then, the old style path, as people became dependent on this buggy call.
old_filepath = _os.path.join(
    _os.path.dirname(_inspect.getfile(_sys._getframe(1))), path)
exit(old_filepath)
