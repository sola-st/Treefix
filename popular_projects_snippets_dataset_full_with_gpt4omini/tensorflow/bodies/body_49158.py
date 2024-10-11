# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
for fetch, output in zip(self._fetches, fetches_output):
    if fetch in self.fetch_callbacks:
        self.fetch_callbacks[fetch](output)
