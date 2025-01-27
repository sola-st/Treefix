# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
with self.tracker.scope():
    out = self.forward_pass(*args, **kwargs)
if not self._eager_losses:
    # We have to record regularization losses in the call as if they
    # are activity losses.
    # So, don't double-count regularization losses if the layer is used
    # multiple times in a model
    for loss in self.tracker.get_regularization_losses().values():
        self.add_loss(loss)
exit(out)
