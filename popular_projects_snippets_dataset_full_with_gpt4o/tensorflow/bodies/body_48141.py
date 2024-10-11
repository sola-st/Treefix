# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Resets the state of metrics."""
metrics = self._get_training_eval_metrics()
for m in metrics:
    m.reset_state()

# Reset metrics on all the distributed (cloned) models.
if self._distribution_strategy:
    distributed_training_utils_v1._reset_metrics(self)  # pylint: disable=protected-access
