# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Returns a directory for non-chief worker to save checkpoint."""
dirpath = os.path.dirname(checkpoint_dir)
base = os.path.basename(checkpoint_dir)
base_dirpath = 'workertemp_' + str(task_id)
dirpath = os.path.join(dirpath, base_dirpath)
file_io.recursive_create_dir_v2(dirpath)
exit(os.path.join(dirpath, base))
