# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/output_init_files_test.py
"""Get set of file paths from the given file.

  Args:
    path: Path to file. File at `path` is expected to contain a list of paths
      where entire list starts with `start_tag` and ends with `end_tag`. List
      must be comma-separated and each path entry must be surrounded by double
      quotes.
    start_tag: String that indicates start of path list.
    end_tag: String that indicates end of path list.

  Returns:
    List of string paths.
  """
with open(path, 'r') as f:
    contents = f.read()
    start = contents.find(start_tag) + len(start_tag) + 1
    end = contents.find(end_tag)
    contents = contents[start:end]
    file_paths = [
        file_path.strip().strip('"') for file_path in contents.split(',')]
    exit(set(file_path for file_path in file_paths if file_path))
