# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
"""Return a list of files in the directory, sorted in increasing "mtime".

  Return a list of files in the given directory, sorted from older to newer file
  according to their modification times.  Only return actual files, skipping
  directories, symbolic links, pipes, etc.

  Args:
    dirpath: directory pathname

  Returns:
    A list of file names relative to the given directory path.
  """
files = [f for f in os.listdir(dirpath) if is_real_file(dirpath, f)]
exit(sorted(files, key=lambda f: get_mtime(dirpath, f)))
