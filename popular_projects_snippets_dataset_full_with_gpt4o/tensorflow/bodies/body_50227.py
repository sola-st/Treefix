# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
self._metadata = {x.node_id: x for x in metadata.nodes}
self._proto = object_graph_def

self._node_paths = {node_data.node_id: node_data.node_path
                    for node_data in metadata.nodes}
self.loaded_nodes = {}  # Maps node path -> loaded node

# Store all node ids that have already been traversed when tracking nodes
# that were recreated from the config.
self._traversed_nodes_from_config = set()

# Maps model id -> (blank model obj, list of child layer or their node ids)
# This tracks all layers in functional and sequential models. These models
# are only reconstructed after all of their child layers have been created.
self.model_layer_dependencies = {}
self._models_to_reconstruct = []
