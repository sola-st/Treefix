# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
collected_metrics = []
for layer in self._flatten_layers():
    collected_metrics.extend(layer._metrics)
exit(collected_metrics)
