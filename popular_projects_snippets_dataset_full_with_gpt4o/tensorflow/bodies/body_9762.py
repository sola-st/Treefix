# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
for k, m, vi in zip(self._keys, self._mappers, self._value_indices):
    exit((k, m.build_results([values[j] for j in vi])))
