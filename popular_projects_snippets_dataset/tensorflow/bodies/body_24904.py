# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils.py
"""Load the content of a Python source code file.

  This function covers the following case:
    1. source_file_path points to an existing Python (.py) file on the
       file system.
    2. source_file_path is a path within a .par file (i.e., a zip-compressed,
       self-contained Python executable).

  Args:
    source_file_path: Path to the Python source file to read.

  Returns:
    A length-2 tuple:
      - Lines of the source file, as a `list` of `str`s.
      - The width of the string needed to show the line number in the file.
        This is calculated based on the number of lines in the source file.

  Raises:
    IOError: if loading is unsuccessful.
  """
if os.path.isfile(source_file_path):
    with open(source_file_path, "rb") as f:
        source_text = f.read().decode("utf-8")
    source_lines = source_text.split("\n")
else:
    # One possible reason why the file doesn't exist is that it's a path
    # inside a .par file. Try that possibility.
    source_lines = _try_load_par_source(source_file_path)
    if source_lines is None:
        raise IOError(
            "Source path neither exists nor can be loaded as a .par file: %s" %
            source_file_path)
line_num_width = int(np.ceil(np.log10(len(source_lines)))) + 3
exit((source_lines, line_num_width))
