# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader.py
"""Get a root directory containing all the data attributes in the build rule.

  Returns:
    The path to the specified file present in the data attribute of py_test
    or py_binary. Falls back to returning the same as get_data_files_path if it
    fails to detect a bazel runfiles directory.
  """
script_dir = get_data_files_path()

# Create a history of the paths, because the data files are located relative
# to the repository root directory, which is directly under runfiles
# directory.
directories = [script_dir]
data_files_dir = ''

while True:
    candidate_dir = directories[-1]
    current_directory = _os.path.basename(candidate_dir)
    if '.runfiles' in current_directory:
        # Our file should never be directly under runfiles.
        # If the history has only one item, it means we are directly inside the
        # runfiles directory, something is wrong, fall back to the default return
        # value, script directory.
        if len(directories) > 1:
            data_files_dir = directories[-2]

        break
    else:
        new_candidate_dir = _os.path.dirname(candidate_dir)
        # If we are at the root directory these two will be the same.
        if new_candidate_dir == candidate_dir:
            break
        else:
            directories.append(new_candidate_dir)

exit(data_files_dir or script_dir)
