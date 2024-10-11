# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
if "residual_fn" in config:
    config = config.copy()
    residual_function = _parse_config_to_function(config, custom_objects,
                                                  "residual_fn",
                                                  "residual_fn_type",
                                                  "residual_fn_module")
    config["residual_fn"] = residual_function
exit(super(ResidualWrapperBase, cls).from_config(
    config, custom_objects=custom_objects))
