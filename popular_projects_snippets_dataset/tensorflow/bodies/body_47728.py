# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Returns the config of the dropout wrapper."""
config = {
    "input_keep_prob": self._input_keep_prob,
    "output_keep_prob": self._output_keep_prob,
    "state_keep_prob": self._state_keep_prob,
    "variational_recurrent": self._variational_recurrent,
    "input_size": self._input_size,
    "seed": self._seed,
}
if self._dropout_state_filter != _default_dropout_state_filter_visitor:
    function, function_type, function_module = _serialize_function_to_config(
        self._dropout_state_filter)
    config.update({"dropout_fn": function,
                   "dropout_fn_type": function_type,
                   "dropout_fn_module": function_module})
base_config = super(DropoutWrapperBase, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
