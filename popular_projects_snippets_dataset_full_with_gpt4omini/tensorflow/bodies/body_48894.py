# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
training_mode = None
if self._expects_training_arg:
    # (1) `training` was passed to this `Layer.call`.
    if self._call_arg_was_passed('training', args, kwargs):
        training_mode = self._get_call_arg_value('training', args, kwargs)
    # If no `training` arg was passed, or `None` was explicitly passed,
    # the framework will make a decision about the training mode is.
    if training_mode is None:
        call_ctx_training = call_context.training
        # (2) `training` mode is inferred from an outer `Layer.call`.
        if call_ctx_training is not None:
            training_mode = call_ctx_training
        # (3) User set `tf.keras.backend.set_learning_phase`.
        elif backend.global_learning_phase_is_set():
            training_mode = backend.learning_phase()
            # Ensure value is a `bool` or `tf.bool`.
            if isinstance(training_mode, bool):
                pass
            elif tensor_util.is_tf_type(training_mode):
                training_mode = math_ops.cast(training_mode, dtypes.bool)
            else:
                training_mode = bool(training_mode)
        # (4) We default to using `call`'s default value for `training`,
        # or treating the layer as if it is in inference if no non-None default
        # is specified in the `call` signature.
        else:
            training_mode = self._default_training_arg

        # For case (2), (3), (4) `training` arg is passed by framework.
        args, kwargs = self._set_call_arg_value('training', training_mode, args,
                                                kwargs)
else:
    if 'training' in kwargs:
        # `training` was passed to this `Layer` but is not needed for
        # `Layer.call`. It will set the default mode for inner `Layer.call`s.
        training_mode = kwargs.pop('training')
    else:
        # Grab the current `training` mode from any outer `Layer.call`.
        training_mode = call_context.training

exit((args, kwargs, training_mode))
