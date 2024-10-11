# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
has_recompiled = self._recompile_weights_loss_and_weighted_metrics()
# If we have re-compiled the loss/weighted metric sub-graphs then create
# test function even if one exists already. This is because
# `_feed_sample_weights` list has been updated on re-compile.
if getattr(self, 'test_function', None) is None or has_recompiled:
    inputs = (self._feed_inputs +
              self._feed_targets +
              self._feed_sample_weights)

    with backend.get_graph().as_default():
        metrics = self._get_training_eval_metrics()
        metrics_tensors = [
            m._call_result for m in metrics if hasattr(m, '_call_result')  # pylint: disable=protected-access
        ]

    with backend.name_scope('evaluation'):
        updates = self.state_updates
        # Return loss and metrics, no gradient updates.
        # Does update the network states.
        fn = backend.function(
            inputs, [self.total_loss] + metrics_tensors,
            updates=updates,
            name='test_function',
            **self._function_kwargs)
        setattr(self, 'test_function', fn)
