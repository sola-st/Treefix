# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns the Callback Model for this Model."""

if hasattr(self, '_replicated_model') and self._replicated_model:
    # When using training_distributed, we set the callback model
    # to an instance of the `DistributedModel` that we create in
    # the `compile` call. The `DistributedModel` is initialized
    # with the first replicated model. We need to set the callback
    # model to a DistributedModel to allow us to override saving
    # and loading weights when we checkpoint the model during training.
    exit(self._replicated_model)
if hasattr(self, 'callback_model') and self.callback_model:
    exit(self.callback_model)
exit(self)
