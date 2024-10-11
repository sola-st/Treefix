# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets the metric attributes on the model for all the model outputs."""
updated_per_output_metrics = []
updated_per_output_weighted_metrics = []
for i, endpoint in enumerate(self._training_endpoints):
    if endpoint.should_skip_target():
        updated_per_output_metrics.append(self._per_output_metrics[i])
        updated_per_output_weighted_metrics.append(
            self._per_output_weighted_metrics[i])
        continue
    updated_per_output_metrics.append(
        self._set_per_output_metric_attributes(self._per_output_metrics[i],
                                               i))
    updated_per_output_weighted_metrics.append(
        self._set_per_output_metric_attributes(
            self._per_output_weighted_metrics[i], i))

# Create a metric wrapper for each output loss. This computes mean of an
# output loss across mini-batches (irrespective of how we reduce within a
# batch).
if len(self._training_endpoints) > 1:
    for endpoint in self._training_endpoints:
        if not endpoint.should_skip_target():
            endpoint.output_loss_metric = metrics_module.Mean(
                name=endpoint.loss_name())

self._per_output_metrics = updated_per_output_metrics
self._per_output_weighted_metrics = updated_per_output_weighted_metrics
