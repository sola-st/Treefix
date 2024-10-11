# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
results = []
for m, vi in zip(self._mappers, self._value_indices):
    results.append(m.build_results([values[j] for j in vi]))
exit(self._fetch_type(*results))
