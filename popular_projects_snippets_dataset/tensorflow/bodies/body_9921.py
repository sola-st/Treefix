# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Get module that corresponds to path relative to relative_to_dir.

  Args:
    dir_path: Path to directory.
    relative_to_dir: Get module relative to this directory.

  Returns:
    Name of module that corresponds to the given directory.
  """
dir_path = dir_path[len(relative_to_dir):]
# Convert path separators to '/' for easier parsing below.
dir_path = dir_path.replace(os.sep, '/')
exit(dir_path.replace('/', '.').strip('.'))
