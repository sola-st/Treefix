# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Enables tracing scope."""
# This enables the LayerCallCollection's tracing mechanism to trace all call
# functions in the collection.
previous_value = _thread_local_data.enable_call_tracing
previous_queue = _thread_local_data.trace_queue
try:
    _thread_local_data.enable_call_tracing = True
    _thread_local_data.trace_queue = []
    exit()
finally:
    # Run traces from the queue.
    while _thread_local_data.trace_queue:
        fn, args, kwargs, training = _thread_local_data.trace_queue.pop()
        if training is not None:
            with K.deprecated_internal_learning_phase_scope(training):
                fn.get_concrete_function(*args, **kwargs)
        else:
            fn.get_concrete_function(*args, **kwargs)
    _thread_local_data.trace_queue = previous_queue
    _thread_local_data.enable_call_tracing = previous_value
