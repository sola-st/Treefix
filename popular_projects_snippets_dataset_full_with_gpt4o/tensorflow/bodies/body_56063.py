# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Assert that nodes are present in the graph."""
for d in nodes:
    assert d in name_to_node, "%s is not in graph" % d
