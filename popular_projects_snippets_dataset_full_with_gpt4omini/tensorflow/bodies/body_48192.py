# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if hasattr(self, '_training_endpoints'):
    exit([
        e.output_loss_metric
        for e in self._training_endpoints
        if e.output_loss_metric is not None
    ])
exit(None)
