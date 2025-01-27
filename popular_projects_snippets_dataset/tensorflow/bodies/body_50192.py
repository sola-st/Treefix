# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Exports model to v1 SavedModel format."""
if not model._is_graph_network:  # pylint: disable=protected-access
    if isinstance(model, sequential.Sequential):
        # If input shape is not directly set in the model, the exported model
        # will infer the expected shapes of the input from the model.
        if not model.built:
            raise ValueError('Weights for sequential model have not yet been '
                             'created. Weights are created when the Model is first '
                             'called on inputs or `build()` is called with an '
                             '`input_shape`, or the first layer in the model has '
                             '`input_shape` during construction.')
        # TODO(kathywu): Build the model with input_signature to create the
        # weights before _export_model_variables().
    else:
        raise NotImplementedError(
            'Subclassed models can only be exported for serving. Please set '
            'argument serving_only=True.')

builder = saved_model_builder._SavedModelBuilder(path)  # pylint: disable=protected-access

# Manually save variables to export them in an object-based checkpoint. This
# skips the `builder.add_meta_graph_and_variables()` step, which saves a
# named-based checkpoint.
# TODO(b/113134168): Add fn to Builder to save with object-based saver.
# TODO(b/113178242): This should only export the model json structure. Only
# one save is needed once the weights can be copied from the model to clone.
checkpoint_path = _export_model_variables(model, path)

# Export each mode. Use ModeKeys enums defined for `Estimator` to ensure that
# Keras models and `Estimator`s are exported with the same format.
# Every time a mode is exported, the code checks to see if new variables have
# been created (e.g. optimizer slot variables). If that is the case, the
# checkpoint is re-saved to include the new variables.
export_args = {'builder': builder,
               'model': model,
               'custom_objects': custom_objects,
               'checkpoint_path': checkpoint_path,
               'input_signature': input_signature}

has_saved_vars = False
if model.optimizer:
    if isinstance(model.optimizer, (optimizer_v1.TFOptimizer,
                                    optimizer_v2.OptimizerV2)):
        _export_mode(mode_keys.ModeKeys.TRAIN, has_saved_vars, **export_args)
        has_saved_vars = True
        _export_mode(mode_keys.ModeKeys.TEST, has_saved_vars, **export_args)
    else:
        logging.warning(
            'Model was compiled with an optimizer, but the optimizer is not from '
            '`tf.train` (e.g. `tf.train.AdagradOptimizer`). Only the serving '
            'graph was exported. The train and evaluate graphs were not added to '
            'the SavedModel.')
_export_mode(mode_keys.ModeKeys.PREDICT, has_saved_vars, **export_args)

builder.save(as_text)
