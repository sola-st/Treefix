# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Container for `Callback` instances.

    This object wraps a list of `Callback` instances, making it possible
    to call them all at once via a single endpoint
    (e.g. `callback_list.on_epoch_end(...)`).

    Args:
      callbacks: List of `Callback` instances.
      add_history: Whether a `History` callback should be added, if one does not
        already exist in the `callbacks` list.
      add_progbar: Whether a `ProgbarLogger` callback should be added, if one
        does not already exist in the `callbacks` list.
      model: The `Model` these callbacks are used with.
      **params: If provided, parameters will be passed to each `Callback` via
        `Callback.set_params`.
    """
self.callbacks = nest.flatten(callbacks) if callbacks else []
self._add_default_callbacks(add_history, add_progbar)

if model:
    self.set_model(model)
if params:
    self.set_params(params)

# Performance optimization: determines if batch hooks need to be called.
# pylint: disable=protected-access
self._supports_tf_logs = all(
    getattr(cb, '_supports_tf_logs', False) for cb in self.callbacks)
self._batch_hooks_support_tf_logs = all(
    getattr(cb, '_supports_tf_logs', False)
    for cb in self.callbacks
    if cb._implements_train_batch_hooks() or cb
    ._implements_test_batch_hooks() or cb._implements_predict_batch_hooks())

self._should_call_train_batch_hooks = any(
    cb._implements_train_batch_hooks() for cb in self.callbacks)
self._should_call_test_batch_hooks = any(
    cb._implements_test_batch_hooks() for cb in self.callbacks)
self._should_call_predict_batch_hooks = any(
    cb._implements_predict_batch_hooks() for cb in self.callbacks)
# pylint: enable=protected-access

self._disallow_batch_hooks_in_ps_strategy()

# Performance check: Check batch hooks for slowness compared to batch time.
# Only run check for custom callbacks (i.e. not present in this file).
self._check_timing = any(
    cbk.__class__.__name__ not in globals() for cbk in self.callbacks)
self._num_batches_for_timing_check = 5
self._hook_times = {}
self._batch_start_time = None
self._batch_times = []
