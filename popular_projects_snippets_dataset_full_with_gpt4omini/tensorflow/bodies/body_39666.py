# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
for child in object_metadata.nodes[0].children:
    if child.local_name == "lookup_table":
        exit(object_metadata.nodes[child.node_id])
