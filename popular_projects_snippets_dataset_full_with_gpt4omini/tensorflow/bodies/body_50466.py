# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Error out if batch-level callbacks are passed with PSStrategy."""
# pylint: disable=protected-access
strategy = ds_context.get_strategy()
if strategy._should_use_with_coordinator:
    unsupported_callbacks = []
    for cb in self.callbacks:
        # These Callbacks can accept RemoteValues directly.
        if getattr(cb, '_supports_tf_logs', False):
            continue
        if (cb._implements_train_batch_hooks() or
            cb._implements_test_batch_hooks() or
            cb._implements_predict_batch_hooks()):
            unsupported_callbacks.append(cb)
    if unsupported_callbacks:
        raise ValueError('Batch-level `Callback`s are not supported with '
                         '`ParameterServerStrategy`. Found unsupported '
                         'callbacks: {}'.format(unsupported_callbacks))
