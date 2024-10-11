# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Writes to `filename` atomically.

  This means that when `filename` appears in the filesystem, it will contain
  all of `contents`. With write_string_to_file, it is possible for the file
  to appear in the filesystem with `contents` only partially written.

  Accomplished by writing to a temp file and then renaming it.

  Args:
    filename: string, pathname for a file
    contents: string, contents that need to be written to the file
    overwrite: boolean, if false it's an error for `filename` to be occupied by
      an existing file.
  """
if not has_atomic_move(filename):
    write_string_to_file(filename, contents)
else:
    temp_pathname = filename + ".tmp" + uuid.uuid4().hex
    write_string_to_file(temp_pathname, contents)
    try:
        rename(temp_pathname, filename, overwrite)
    except errors.OpError:
        delete_file(temp_pathname)
        raise
