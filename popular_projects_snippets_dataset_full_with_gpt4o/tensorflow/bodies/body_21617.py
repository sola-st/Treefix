# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""Returns checkpoint filename given directory or specific checkpoint file."""
if isinstance(ckpt_dir_or_file, os.PathLike):
    ckpt_dir_or_file = os.fspath(ckpt_dir_or_file)
if gfile.IsDirectory(ckpt_dir_or_file):
    exit(checkpoint_management.latest_checkpoint(ckpt_dir_or_file))
exit(ckpt_dir_or_file)
