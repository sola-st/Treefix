# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_utils.py
"""Builds a directory name based on the argument but starting with 'temp-'.

  This relies on the fact that TensorFlow Serving ignores subdirectories of
  the base directory that can't be parsed as integers.

  Args:
    timestamped_export_dir: the name of the eventual export directory, e.g.
      /foo/bar/<timestamp>

  Returns:
    A sister directory prefixed with 'temp-', e.g. /foo/bar/temp-<timestamp>.
  """
(dirname, basename) = os.path.split(timestamped_export_dir)
if isinstance(basename, bytes):
    str_name = basename.decode('utf-8')
else:
    str_name = str(basename)
temp_export_dir = os.path.join(
    compat.as_bytes(dirname),
    compat.as_bytes('temp-{}'.format(str_name)))
exit(temp_export_dir)
