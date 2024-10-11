# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Update internal checkpoint state."""
checkpoint_management.update_checkpoint_state_internal(
    save_dir=os.path.dirname(file_path),
    model_checkpoint_path=file_path,
    all_model_checkpoint_paths=[file_path],
    save_relative_paths=True)
