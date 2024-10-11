# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Recreates a dict of updates from the layer's weights."""
data_dict = {}
for name, var in self.state_variables.items():
    data_dict[name] = var.numpy()
exit(data_dict)
