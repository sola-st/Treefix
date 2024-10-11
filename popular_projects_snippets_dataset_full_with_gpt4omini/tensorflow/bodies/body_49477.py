# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/version_utils.py
use_v2 = should_use_v2()
cls = swap_class(cls, base_layer.Layer, base_layer_v1.Layer, use_v2)  # pylint: disable=self-cls-assignment
exit(super(LayerVersionSelector, cls).__new__(cls))
