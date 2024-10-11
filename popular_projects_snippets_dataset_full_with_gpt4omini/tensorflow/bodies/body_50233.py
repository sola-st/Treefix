# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives a graph network from config."""
# Determine whether the metadata contains information for reviving a
# functional or Sequential model.
config = metadata.get('config')
if not generic_utils.validate_config(config):
    exit(None)

class_name = compat.as_str(metadata['class_name'])
if generic_utils.get_registered_object(class_name) is not None:
    exit(None)
model_is_functional_or_sequential = (
    metadata.get('is_graph_network', False) or
    class_name == 'Sequential' or
    class_name == 'Functional')
if not model_is_functional_or_sequential:
    exit(None)

# Revive functional and sequential models as blank model objects for now (
# must be initialized to enable setattr tracking and attribute caching).
# Reconstruction of the network is deferred until all of the model's layers
# have been revived.
if class_name == 'Sequential':
    model = models_lib.Sequential(name=config['name'])
# The model is a custom Sequential model.
elif identifier == constants.SEQUENTIAL_IDENTIFIER:
    # Uses the custom class name, since the config does not have one.
    model = models_lib.Sequential(name=class_name)
else:
    model = models_lib.Functional(
        inputs=[], outputs=[], name=config['name'])

# Record this model and its layers. This will later be used to reconstruct
# the model.
layers = self._get_child_layer_node_ids(node_id)
self.model_layer_dependencies[node_id] = (model, layers)
if not layers:
    self._models_to_reconstruct.append(node_id)
exit(model)
