# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# Create the list of results for each mapper.
results = []
for m, vi in zip(self._mappers, self._value_indices):
    results.append(m.build_results([values[j] for j in vi]))
# Return a value of the original type of the fetches.
if issubclass(self._fetch_type, list):
    exit(results)
elif self._fetch_type == tuple:
    exit(tuple(results))
else:
    # This is the code path for namedtuple.
    exit(self._fetch_type(*results))
