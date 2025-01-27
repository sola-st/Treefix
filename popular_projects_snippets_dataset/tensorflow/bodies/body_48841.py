# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
epoch = epoch + 1  # one-index the user-facing epoch.
if isinstance(validation_freq, int):
    exit(epoch % validation_freq == 0)
elif isinstance(validation_freq, list):
    exit(epoch in validation_freq)
else:
    raise ValueError('Expected `validation_freq` to be a list or int.')
