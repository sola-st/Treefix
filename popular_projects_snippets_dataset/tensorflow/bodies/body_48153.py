# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Prepare sample weight modes. List with the same length as model outputs.
training_utils_v1.prepare_sample_weight_modes(
    self._training_endpoints, sample_weight_mode)
# Prepare sample weights.
self._prepare_sample_weights()
# Save all metric attributes per output of the model.
self._cache_output_metric_attributes(metrics, weighted_metrics)
self.total_loss = None
# Set metric attributes on model.
self._set_metric_attributes()

self._collected_trainable_weights = self.trainable_weights
