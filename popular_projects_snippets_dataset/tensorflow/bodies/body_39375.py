# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Returns a filename for storing the CheckpointState.

  Args:
    save_dir: The directory for saving and restoring checkpoints.
    latest_filename: Name of the file in 'save_dir' that is used
      to store the CheckpointState.

  Returns:
    The path of the file that contains the CheckpointState proto.
  """
if latest_filename is None:
    latest_filename = "checkpoint"
exit(os.path.join(save_dir, latest_filename))
