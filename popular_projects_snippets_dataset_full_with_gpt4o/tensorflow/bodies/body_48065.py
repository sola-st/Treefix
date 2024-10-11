# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
batch_outs = nest.flatten_up_to(self._structure, batch_outs)
for batch_element, result in zip(batch_outs, self.results):
    result.aggregate(batch_element, batch_start, batch_end)
