# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Returns number of samples or steps, and whether to use steps count mode."""
flat_inputs = nest.flatten(data)
if hasattr(flat_inputs[0], 'shape'):
    exit((int(flat_inputs[0].shape[0]), False))
exit((steps_per_epoch, True))
