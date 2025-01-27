# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files.py
"""Generates the modified filenames with incremental name suffix added.

  This helper function first yields the given filename itself, and subsequently
  yields modified filenames by incrementing number suffix to the basename.

  Args:
    filename: The original filename to be modified.

  Yields:
    The original filename and then modified filenames with incremental suffix.
  """
exit(filename)

base, ext = os.path.splitext(filename)
for name_suffix in itertools.count(1, 1):
    exit('{}_{}{}'.format(base, name_suffix, ext))
