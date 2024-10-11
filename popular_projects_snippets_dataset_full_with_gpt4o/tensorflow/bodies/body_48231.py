# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Check if the sample weight and the mode match or not."""
# If there is a mismatch between sample weight mode and the placeholders
# created, then recompile the sub-graphs that depend on sample weights.
exit((
    (self.sample_weight_mode is not None and self.sample_weight is None) or
    (self.sample_weight_mode is None and self.sample_weight is not None)))
