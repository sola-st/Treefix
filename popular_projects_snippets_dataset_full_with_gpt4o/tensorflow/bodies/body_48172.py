# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
has_recompiled = self._recompile_weights_loss_and_weighted_metrics()
self._check_trainable_weights_consistency()
if isinstance(self.optimizer, list):
    raise ValueError('The `optimizer` in `compile` should be a single '
                     'optimizer.')
# If we have re-compiled the loss/weighted metric sub-graphs then create
# train function even if one exists already. This is because
# `_feed_sample_weights` list has been updated on re-compile.
if getattr(self, 'train_function', None) is None or has_recompiled:
    # Restore the compiled trainable state.
    current_trainable_state = self._get_trainable_state()
    self._set_trainable_state(self._compiled_trainable_state)

    inputs = (self._feed_inputs +
              self._feed_targets +
              self._feed_sample_weights)
    if not isinstance(backend.symbolic_learning_phase(), int):
        inputs += [backend.symbolic_learning_phase()]

    with backend.get_graph().as_default():
        with backend.name_scope('training'):
            # Training updates
            updates = self.optimizer.get_updates(
                params=self._collected_trainable_weights, loss=self.total_loss)
            # Unconditional updates
            updates += self.get_updates_for(None)
            # Conditional updates relevant to this model
            updates += self.get_updates_for(self.inputs)

        metrics = self._get_training_eval_metrics()
        metrics_tensors = [
            m._call_result for m in metrics if hasattr(m, '_call_result')  # pylint: disable=protected-access
        ]

    with backend.name_scope('training'):
        # Gets loss and metrics. Updates weights at each call.
        fn = backend.function(
            inputs, [self.total_loss] + metrics_tensors,
            updates=updates,
            name='train_function',
            **self._function_kwargs)
        setattr(self, 'train_function', fn)

    # Restore the current trainable state
    self._set_trainable_state(current_trainable_state)
