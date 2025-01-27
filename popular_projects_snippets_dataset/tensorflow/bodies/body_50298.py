# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
if tracing_enabled():
    _thread_local_data.trace_queue.append(
        (fn, args[:], kwargs.copy(), training))
