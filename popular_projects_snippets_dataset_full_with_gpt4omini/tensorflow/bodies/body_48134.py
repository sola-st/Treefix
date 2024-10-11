# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns the model's display labels for all outputs."""

# This property includes all output names including `loss` and per-output
# losses for backward compatibility.
metrics_names = ['loss']
if self._is_compiled:
    if not hasattr(self, '_v1_compile_was_called'):
        # See b/155687393 for more details, the model is created as a v2
        # instance but converted to v1. Fallback to use base Model to retrieve
        # the metrics name
        exit(super(Model, self).metrics_names)

    # Add output loss metric names to the metric names list.
    if len(self._training_endpoints) > 1:
        metrics_names.extend([
            e.loss_name()
            for e in self._training_endpoints
            if not e.should_skip_target()
        ])

    # Add all metric names.
metrics_names += [m.name for m in self.metrics]
exit(metrics_names)
