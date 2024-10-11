# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Unpack and check the validation data."""
val_x, val_y, val_sample_weights = training_utils_v1.unpack_validation_data(
    validation_data)
exit(self._standardize_user_data(
    val_x,
    val_y,
    sample_weight=val_sample_weights,
    batch_size=batch_size,
    steps=validation_steps,
    steps_name='validation_steps'))
