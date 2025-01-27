# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Returns the config of the residual wrapper."""
if self._residual_fn is not None:
    function, function_type, function_module = _serialize_function_to_config(
        self._residual_fn)
    config = {
        "residual_fn": function,
        "residual_fn_type": function_type,
        "residual_fn_module": function_module
    }
else:
    config = {}
base_config = super(ResidualWrapperBase, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
