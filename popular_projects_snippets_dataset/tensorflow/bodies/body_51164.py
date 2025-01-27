# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_utils.py
"""Builds a path to a new subdirectory within the base directory.

  Each export is written into a new subdirectory named using the
  current time.  This guarantees monotonically increasing version
  numbers even across multiple runs of the pipeline.
  The timestamp used is the number of seconds since epoch UTC.

  Args:
    export_dir_base: A string containing a directory to write the exported
        graph and checkpoints.
  Returns:
    The full path of the new subdirectory (which is not actually created yet).

  Raises:
    RuntimeError: if repeated attempts fail to obtain a unique timestamped
      directory name.
  """
attempts = 0
while attempts < MAX_DIRECTORY_CREATION_ATTEMPTS:
    timestamp = int(time.time())

    result_dir = file_io.join(
        compat.as_bytes(export_dir_base), compat.as_bytes(str(timestamp)))
    if not gfile.Exists(result_dir):
        # Collisions are still possible (though extremely unlikely): this
        # directory is not actually created yet, but it will be almost
        # instantly on return from this function.
        exit(result_dir)
    time.sleep(1)
    attempts += 1
    logging.warn('Directory {} already exists; retrying (attempt {}/{})'.format(
        compat.as_str(result_dir), attempts, MAX_DIRECTORY_CREATION_ATTEMPTS))
raise RuntimeError('Failed to obtain a unique export directory name after '
                   f'{MAX_DIRECTORY_CREATION_ATTEMPTS} attempts.')
