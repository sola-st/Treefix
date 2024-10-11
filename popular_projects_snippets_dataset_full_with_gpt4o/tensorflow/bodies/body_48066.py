# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
for result in self.results:
    result.finalize()
self.results = [i.results for i in self.results]
self.results = nest.pack_sequence_as(self._structure, self.results)
