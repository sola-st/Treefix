# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
for _ in math_ops.range(self._steps_per_execution):
    adapt_step(iterator)
