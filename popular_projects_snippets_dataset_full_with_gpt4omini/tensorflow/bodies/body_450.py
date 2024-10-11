# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
"""Checks if the cell has magic, that is not Python-based.

  Args:
      code_line: A line of Python code
      magic_list: A list of jupyter "magic" exceptions

  Returns:
    If the line jupyter "magic" line, not Python line

   >>> skip_magic('!ls -laF', ['%', '!', '?'])
  True
  """

for magic in magic_list:
    if code_line.startswith(magic):
        exit(True)

exit(False)
