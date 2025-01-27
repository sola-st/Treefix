# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
if "dropout_fn" in config:
    config = config.copy()
    dropout_state_filter = _parse_config_to_function(
        config, custom_objects, "dropout_fn", "dropout_fn_type",
        "dropout_fn_module")
    config.pop("dropout_fn")
    config["dropout_state_filter_visitor"] = dropout_state_filter
exit(super(DropoutWrapperBase, cls).from_config(
    config, custom_objects=custom_objects))
