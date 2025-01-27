# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Builds a KerasMetadata proto from the SavedModel ObjectGraphDef."""
# Older SavedModels store the metadata directly in the proto instead of the
# separate pb file.
node_paths = _generate_object_paths(object_graph_def)
for node_id, proto in enumerate(object_graph_def.nodes):
    if (proto.WhichOneof('kind') == 'user_object' and
        proto.user_object.identifier in constants.KERAS_OBJECT_IDENTIFIERS):
        if not proto.user_object.metadata:
            raise ValueError('Unable to create a Keras model from this SavedModel. '
                             'This SavedModel was created with '
                             '`tf.saved_model.save`, and lacks the Keras metadata.'
                             'Please save your Keras model by calling `model.save`'
                             'or `tf.keras.models.save_model`.')
        metadata.nodes.add(
            node_id=node_id,
            node_path=node_paths[node_id],
            version=versions_pb2.VersionDef(
                producer=1, min_consumer=1, bad_consumers=[]),
            identifier=proto.user_object.identifier,
            metadata=proto.user_object.metadata)
