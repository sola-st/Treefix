# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
# Trigger traces of other call functions + extra training-arg traces.
if tracing_enabled():
    self.call_collection.add_trace(*args, **kwargs)
