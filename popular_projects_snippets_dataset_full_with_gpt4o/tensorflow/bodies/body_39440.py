# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Generates dictionary of registered savers and updates the proto."""
registered_savers = collections.defaultdict(dict)
for saver_name, trackables in registered_trackables.items():
    for td in trackables:
        registered_savers[saver_name][td.object_name] = td.object_to_save

        object_proto = object_graph_proto.nodes[td.node_id]
        object_proto.registered_saver.name = saver_name
        object_proto.registered_saver.object_name = td.object_name

exit(registered_savers)
