# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
if not reset_state:
    self._adapt_accumulator = self._combiner.restore(self._restore_updates())
super(CombinerPreprocessingLayer, self).adapt(
    data, batch_size=batch_size, steps=steps, reset_state=reset_state)
