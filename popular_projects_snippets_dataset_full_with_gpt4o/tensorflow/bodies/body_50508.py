# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Instantiate a `Progbar` if not yet, and update the stateful metrics."""
# TODO(rchao): Legacy TF1 code path may use list for
# `self.stateful_metrics`. Remove "cast to set" when TF1 support is dropped.
self.stateful_metrics = set(self.stateful_metrics)

if self.model:
    # Update the existing stateful metrics as `self.model.metrics` may contain
    # updated metrics after `MetricsContainer` is built in the first train
    # step.
    self.stateful_metrics = self.stateful_metrics.union(
        set(m.name for m in self.model.metrics))

if self.progbar is None:
    self.progbar = Progbar(
        target=self.target,
        verbose=self.verbose,
        stateful_metrics=self.stateful_metrics,
        unit_name='step' if self.use_steps else 'sample')

self.progbar._update_stateful_metrics(self.stateful_metrics)  # pylint: disable=protected-access
