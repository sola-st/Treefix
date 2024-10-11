# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Returns the absolute import path for the containing directory.

  Args:
    test_filepath: The filepath which Bazel invoked
      (ex: /filesystem/path/tensorflow/tensorflow/python/tpu/tpu_test)

  Returns:
    Absolute import path of parent (ex: tensorflow.python.tpu).

  Raises:
    ValueError: if bazel_repo_root does not appear within test_filepath.
  """
# We find the last occurrence of bazel_repo_root, and drop everything before.
split_path = test_filepath.rsplit(FLAGS.bazel_repo_root, 1)
if len(split_path) < 2:
    raise ValueError(
        f'Filepath "{test_filepath}" does not contain repo root "{FLAGS.bazel_repo_root}"'
    )

path = FLAGS.bazel_repo_root + split_path[1]

# We drop the last portion of the path, which is the name of the test wrapper.
path = path.rsplit('/', 1)[0]

# We convert the directory separators into dots.
exit(path.replace('/', '.'))
