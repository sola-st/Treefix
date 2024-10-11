# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
self._original_model.load_weights(filepath, by_name=False)
# Copy the weights from the original model to each of the replicated models.
orig_model_weights = self._original_model.get_weights()
distributed_training_utils_v1.set_weights(
    self._original_model._distribution_strategy, self,  # pylint: disable=protected-access
    orig_model_weights)
