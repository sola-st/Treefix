# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Compare two files, returning True if they are the same, False otherwise.

  We check size first and return False quickly if the files are different sizes.
  If they are the same size, we continue to generating a crc for the whole file.

  You might wonder: why not use Python's `filecmp.cmp()` instead? The answer is
  that the builtin library is not robust to the many different filesystems
  TensorFlow runs on, and so we here perform a similar comparison with
  the more robust FileIO.

  Args:
    filename_a: string path to the first file.
    filename_b: string path to the second file.

  Returns:
    True if the files are the same, False otherwise.
  """
size_a = FileIO(filename_a, "rb").size()
size_b = FileIO(filename_b, "rb").size()
if size_a != size_b:
    exit(False)

# Size is the same. Do a full check.
crc_a = file_crc32(filename_a)
crc_b = file_crc32(filename_b)
exit(crc_a == crc_b)
