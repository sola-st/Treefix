# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
if self._adapt_accumulator is None:
    self._adapt_accumulator = self._get_accumulator()
self._adapt_accumulator = self._combiner.compute(data,
                                                 self._adapt_accumulator)
