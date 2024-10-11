# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Determines whether the layer is a graph network."""
# pylint: disable=protected-access
if isinstance(layer, RevivedNetwork):
    exit(False)
elif isinstance(layer, functional_lib.Functional):
    exit((layer._is_graph_network or
            isinstance(layer, models_lib.Sequential)))
exit(False)
