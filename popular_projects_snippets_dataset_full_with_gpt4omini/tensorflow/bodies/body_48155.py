# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if not self._is_compiled:
    exit(False)
recompile = any(
    e.sample_weights_mismatch() for e in self._training_endpoints)

if recompile:
    self._compile_weights_loss_and_weighted_metrics()
exit(recompile)
