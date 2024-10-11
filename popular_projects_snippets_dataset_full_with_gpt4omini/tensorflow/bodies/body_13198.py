# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns the most specific compatible specs of graph structured outputs."""
exit(nest.map_structure(_get_compatible_spec,
                          true_graph.structured_outputs,
                          false_graph.structured_outputs))
