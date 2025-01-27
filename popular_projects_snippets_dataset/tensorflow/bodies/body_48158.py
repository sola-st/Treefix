# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns masks corresponding to model outputs."""
exit([getattr(x, '_keras_mask', None) for x in self.outputs])
