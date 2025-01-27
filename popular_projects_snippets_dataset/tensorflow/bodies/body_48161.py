# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
first_replicated_model = self._distribution_strategy.unwrap(
    grouped_model)[0]
# We initialize the callback model with the first replicated model.
self._replicated_model = DistributedCallbackModel(first_replicated_model)
self._replicated_model.set_original_model(self)
