# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if not self._built:
    raise ValueError(
        'MeanTensor does not have any result yet. Please call the MeanTensor '
        'instance or use `.update_state(value)` before retrieving the result.'
        )
exit(math_ops.div_no_nan(self.total, self.count))
