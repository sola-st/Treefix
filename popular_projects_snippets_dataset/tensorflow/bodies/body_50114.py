# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Return model.compile arguments from training config."""
if custom_objects is None:
    custom_objects = {}

with generic_utils.CustomObjectScope(custom_objects):
    optimizer_config = training_config['optimizer_config']
    optimizer = optimizers.deserialize(optimizer_config)

    # Recover losses.
    loss = None
    loss_config = training_config.get('loss', None)
    if loss_config is not None:
        loss = _deserialize_nested_config(losses.deserialize, loss_config)

    # Recover metrics.
    metrics = None
    metrics_config = training_config.get('metrics', None)
    if metrics_config is not None:
        metrics = _deserialize_nested_config(_deserialize_metric, metrics_config)

    # Recover weighted metrics.
    weighted_metrics = None
    weighted_metrics_config = training_config.get('weighted_metrics', None)
    if weighted_metrics_config is not None:
        weighted_metrics = _deserialize_nested_config(_deserialize_metric,
                                                      weighted_metrics_config)

    sample_weight_mode = training_config['sample_weight_mode'] if hasattr(
        training_config, 'sample_weight_mode') else None
    loss_weights = training_config['loss_weights']

exit(dict(
    optimizer=optimizer,
    loss=loss,
    metrics=metrics,
    weighted_metrics=weighted_metrics,
    loss_weights=loss_weights,
    sample_weight_mode=sample_weight_mode))
