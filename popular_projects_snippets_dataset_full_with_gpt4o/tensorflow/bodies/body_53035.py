# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two repeated node fields."""
exit(_GraphMerger.merge_lists(repeated_nodes1, repeated_nodes2,
                                node_def_pb2.NodeDef, lambda n: n.name,
                                _GraphMerger.merge_nodes))
