# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Tracks the given variable for initialization."""
if context.executing_eagerly():
    exit()
graph = v.graph if hasattr(v, 'graph') else get_graph()
_GRAPH_VARIABLES[graph].add(v)
