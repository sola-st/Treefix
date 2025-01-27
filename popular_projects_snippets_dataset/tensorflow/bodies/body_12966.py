# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Indicates the object shall support gradient ops.

    This function is internally used by _EagerPyFuncGrad to support
    graph mode gradient of EagerFunc via tf.gradient().
    """
self._support_graph_mode_gradient = True
