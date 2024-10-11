# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Fills the object graph proto with data about the registered savers."""
registered_savers = collections.defaultdict(dict)
for saver_name, trackables in unmapped_registered_savers.items():
    for object_name, trackable in trackables.items():
        object_proto = object_graph_proto.nodes[node_ids[trackable]]
        object_proto.registered_saver.name = saver_name
        object_proto.registered_saver.object_name = object_name

        object_to_save = util.get_mapped_trackable(trackable, object_map)
        registered_savers[saver_name][object_name] = object_to_save
exit(registered_savers)
