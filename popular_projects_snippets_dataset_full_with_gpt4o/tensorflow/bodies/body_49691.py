# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
"""Prints a summary for a single layer.

    Args:
        layer: target layer.
    """
try:
    output_shape = layer.output_shape
except AttributeError:
    output_shape = 'multiple'
except RuntimeError:  # output_shape unknown in Eager mode.
    output_shape = '?'
name = layer.name
cls_name = layer.__class__.__name__
if not layer.built and not getattr(layer, '_is_graph_network', False):
    # If a subclassed model has a layer that is not called in Model.call, the
    # layer will not be built and we cannot call layer.count_params().
    params = '0 (unused)'
else:
    params = layer.count_params()
fields = [name + ' (' + cls_name + ')', output_shape, params]
print_row(fields, positions)
