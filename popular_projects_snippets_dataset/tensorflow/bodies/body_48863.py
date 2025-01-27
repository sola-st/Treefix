# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
increment = 'steps' if is_dataset else 'samples'
msg = 'Train on {0} {increment}'.format(
    num_samples_or_steps, increment=increment)
if val_samples_or_steps:
    msg += ', validate on {0} {increment}'.format(
        val_samples_or_steps, increment=increment)
print(msg)
