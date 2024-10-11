# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if self._iterations is not None:
    raise RuntimeError("Cannot set `iterations` to a new Variable after "
                       "the Optimizer weights have been created")
self._iterations = variable
self._weights.append(self._iterations)
