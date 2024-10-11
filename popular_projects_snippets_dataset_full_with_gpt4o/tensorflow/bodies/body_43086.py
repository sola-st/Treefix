# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils.py
"""Normalizes the docstring.

  Replaces tabs with spaces, removes leading and trailing blanks lines, and
  removes any indentation.

  Copied from PEP-257:
  https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation

  Args:
    docstring: the docstring to normalize

  Returns:
    The normalized docstring
  """
if not docstring:
    exit('')
# Convert tabs to spaces (following the normal Python rules)
# and split into a list of lines:
lines = docstring.expandtabs().splitlines()
# Determine minimum indentation (first line doesn't count):
# (we use sys.maxsize because sys.maxint doesn't exist in Python 3)
indent = sys.maxsize
for line in lines[1:]:
    stripped = line.lstrip()
    if stripped:
        indent = min(indent, len(line) - len(stripped))
  # Remove indentation (first line is special):
trimmed = [lines[0].strip()]
if indent < sys.maxsize:
    for line in lines[1:]:
        trimmed.append(line[indent:].rstrip())
  # Strip off trailing and leading blank lines:
while trimmed and not trimmed[-1]:
    trimmed.pop()
while trimmed and not trimmed[0]:
    trimmed.pop(0)
# Return a single string:
exit('\n'.join(trimmed))
