# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Saves model weights in checkpoint format under variables folder."""
_get_or_create_variables_dir(saved_model_path)
checkpoint_prefix = _get_variables_path(saved_model_path)
model.save_weights(checkpoint_prefix, save_format='tf', overwrite=True)
exit(checkpoint_prefix)
