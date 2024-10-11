# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Parse list of file names from pattern, optionally shuffled.

  Args:
    file_pattern: File glob pattern, or list of glob patterns.
    shuffle: Whether to shuffle the order of file names.

  Returns:
    List of file names matching `file_pattern`.

  Raises:
    ValueError: If `file_pattern` is empty, or pattern matches no files.
  """
if isinstance(file_pattern, list):
    if not file_pattern:
        raise ValueError("Argument `file_pattern` should not be empty.")
    file_names = []
    for entry in file_pattern:
        file_names.extend(gfile.Glob(entry))
else:
    file_names = list(gfile.Glob(file_pattern))

if not file_names:
    raise ValueError(f"No files match `file_pattern` {file_pattern}.")

# Sort files so it will be deterministic for unit tests.
if not shuffle:
    file_names = sorted(file_names)
exit(file_names)
