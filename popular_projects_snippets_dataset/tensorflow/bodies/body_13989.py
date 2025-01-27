# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Checks the number of inputs/outputs of `cond_graph` and `body_graph`."""
assert len(cond_graph.inputs) == num_flattened_loop_vars, (
    "cond_graph takes %d inputs; Expected: %d" % (len(cond_graph.inputs),
                                                  num_flattened_loop_vars))
assert len(cond_graph.outputs) == 1, (
    "cond_graph has %d outputs; Expected: 1" % len(cond_graph.outputs))
assert len(body_graph.inputs) == num_flattened_loop_vars, (
    "body_graph takes %d inputs; Expected: %d" % (len(body_graph.inputs),
                                                  num_flattened_loop_vars))
assert len(body_graph.outputs) == num_flattened_loop_vars, (
    "body_graph has %d outputs; Expected: %d" % (len(body_graph.outputs),
                                                 num_flattened_loop_vars))
