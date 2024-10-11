# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
del user_metrics
self._assert_compile_was_called()
kwargs = {
    'loss': self.loss,
    'metrics': self._compile_metrics,
    'loss_weights': self.loss_weights,
    'sample_weight_mode': self.sample_weight_mode,
    'weighted_metrics': self._compile_weighted_metrics,
}
exit(kwargs)
