# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Reconstructs the network structure of all models."""
all_initialized_models = set()
while self._models_to_reconstruct:
    model_id = self._models_to_reconstruct.pop(0)
    all_initialized_models.add(model_id)
    model, layers = self.model_layer_dependencies[model_id]
    self._reconstruct_model(model_id, model, layers)
    _finalize_config_layers([model])

if all_initialized_models != set(self.model_layer_dependencies.keys()):
    # This should not happen.
    uninitialized_model_ids = (
        set(self.model_layer_dependencies.keys()) - all_initialized_models)
    uninitialized_model_names = [
        self.model_layer_dependencies[model_id][0].name
        for model_id in uninitialized_model_ids]
    raise ValueError('Error when loading from SavedModel -- the following '
                     'models could not be initialized: {}'
                     .format(uninitialized_model_names))
