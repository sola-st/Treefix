# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
# save weights from the distributed model to the original model
distributed_model_weights = self.get_weights()
self._original_model.set_weights(distributed_model_weights)
# TODO(anjalisridhar): Do we need to save the original model here?
# Saving the first replicated model works as well.
self._original_model.save(filepath, overwrite=True, include_optimizer=False)
