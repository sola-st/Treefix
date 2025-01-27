# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
exit([
    self._make_dense_default(k, s, t)
    for k, s, t in zip(self.dense_keys, self.dense_shapes, self.dense_types)
])
