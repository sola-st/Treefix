# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
accumulators = ([self._get_accumulator()] +
                [l._get_accumulator() for l in layers])  # pylint: disable=protected-access
merged_accumulator = self._combiner.merge(accumulators)
self._set_accumulator(merged_accumulator)
