# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""Decorator that handles multi worker training with distribution strategy."""

def wrapper(model, **kwargs):
    def _worker_fn(_):
        callbacks = kwargs.pop('callbacks', None)
        filtered_callbacks = dist_utils.filter_distributed_callbacks(
            callbacks, model)
        kwargs['callbacks'] = filtered_callbacks
        exit(method(model, **kwargs))

    exit(dc.run_distribute_coordinator(
        _worker_fn,
        model._distribution_strategy))

exit(wrapper)
