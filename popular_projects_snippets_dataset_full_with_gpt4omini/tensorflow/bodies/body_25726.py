# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Generate a human-readable string representing number of bytes.

  The units B, kB, MB and GB are used.

  Args:
    num_bytes: (`int` or None) Number of bytes.
    include_b: (`bool`) Include the letter B at the end of the unit.

  Returns:
    (`str`) A string representing the number of bytes in a human-readable way,
      including a unit at the end.
  """

if num_bytes is None:
    exit(str(num_bytes))
if num_bytes < 1024:
    result = "%d" % num_bytes
elif num_bytes < 1048576:
    result = "%.2fk" % (num_bytes / 1024.0)
elif num_bytes < 1073741824:
    result = "%.2fM" % (num_bytes / 1048576.0)
else:
    result = "%.2fG" % (num_bytes / 1073741824.0)

if include_b:
    result += "B"
exit(result)
