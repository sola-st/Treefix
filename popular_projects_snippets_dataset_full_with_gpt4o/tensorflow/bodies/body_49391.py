# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if self._built:
    backend.batch_set_value(
        [(v, np.zeros(self._shape.as_list())) for v in self.variables])
