# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save.py
"""Constructs a KerasMetadata proto with the metadata of each keras object."""
metadata = saved_metadata_pb2.SavedMetadata()

for node_id, node in enumerate(saved_nodes):
    if isinstance(node, base_layer.Layer):
        path = node_paths[node]
        if not path:
            node_path = "root"
        else:
            node_path = "root.{}".format(
                ".".join([ref.name for ref in path]))

        metadata.nodes.add(
            node_id=node_id,
            node_path=node_path,
            version=versions_pb2.VersionDef(
                producer=1, min_consumer=1, bad_consumers=[]),
            identifier=node._object_identifier,  # pylint: disable=protected-access
            metadata=node._tracking_metadata)  # pylint: disable=protected-access

exit(metadata)
