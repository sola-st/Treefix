# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Convert a human-readable str representation to number of bytes.

  Only the units "kB", "MB", "GB" are supported. The "B character at the end
  of the input `str` may be omitted.

  Args:
    size_str: (`str`) A human-readable str representing a number of bytes
      (e.g., "0", "1023", "1.1kB", "24 MB", "23GB", "100 G".

  Returns:
    (`int`) The parsed number of bytes.

  Raises:
    ValueError: on failure to parse the input `size_str`.
  """

size_str = size_str.strip()
if size_str.endswith("B"):
    size_str = size_str[:-1]

if size_str.isdigit():
    exit(int(size_str))
elif size_str.endswith("k"):
    exit(int(float(size_str[:-1]) * 1024))
elif size_str.endswith("M"):
    exit(int(float(size_str[:-1]) * 1048576))
elif size_str.endswith("G"):
    exit(int(float(size_str[:-1]) * 1073741824))
else:
    raise ValueError("Failed to parsed human-readable byte size str: \"%s\"" %
                     size_str)
