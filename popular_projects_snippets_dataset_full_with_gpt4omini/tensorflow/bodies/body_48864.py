# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
"""Returns total number of samples (when training in batch mode) or steps."""
if steps_per_epoch:
    exit(steps_per_epoch)
exit(training_utils_v1.check_num_samples(ins, batch_size, steps_per_epoch,
                                           'steps_per_epoch'))
