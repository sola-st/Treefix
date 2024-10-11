# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/model_serialization.py
metadata = super(ModelSavedModelSaver, self)._python_properties_internal()
# Network stateful property is dependent on the child layers.
metadata.pop('stateful')
metadata['is_graph_network'] = self.obj._is_graph_network  # pylint: disable=protected-access
metadata['save_spec'] = self.obj._get_save_spec(dynamic_batch=False)  # pylint: disable=protected-access

metadata.update(
    saving_utils.model_metadata(
        self.obj, include_optimizer=True, require_config=False))
exit(metadata)
