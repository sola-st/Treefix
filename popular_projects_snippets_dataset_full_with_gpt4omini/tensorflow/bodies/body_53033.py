# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two NodeDef messages."""
merged = _GraphMerger.merge_any(node1, node2, node_def_pb2.NodeDef)
merged_inputs = node1.input[:]
merged_inputs.extend([i for i in node2.input[:] if i not in merged_inputs])
merged.input[:] = merged_inputs
exit(merged)
