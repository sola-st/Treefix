# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
callbacks = kwargs.pop('callbacks', None)
filtered_callbacks = dist_utils.filter_distributed_callbacks(
    callbacks, model)
kwargs['callbacks'] = filtered_callbacks
exit(method(model, **kwargs))
