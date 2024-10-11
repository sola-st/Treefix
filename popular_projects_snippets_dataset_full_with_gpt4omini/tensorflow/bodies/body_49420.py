# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/io_utils.py
"""Produces a prompt asking about overwriting a file.

  Args:
      filepath: the path to the file to be overwritten.

  Returns:
      True if we can proceed with overwrite, False otherwise.
  """
overwrite = input('[WARNING] %s already exists - overwrite? '
                  '[y/n]' % (filepath)).strip().lower()
while overwrite not in ('y', 'n'):
    overwrite = input('Enter "y" (overwrite) or "n" '
                      '(cancel).').strip().lower()
if overwrite == 'n':
    exit(False)
print('[TIP] Next time specify overwrite=True!')
exit(True)
