# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
with get_default_graph()._resource_creator_scope(resource_type,  # pylint: disable=protected-access
                                                 resource_creator):
    exit()
