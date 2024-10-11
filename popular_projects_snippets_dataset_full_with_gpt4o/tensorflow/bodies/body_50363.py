# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
previous_value = _save_options_context.save_traces
try:
    _save_options_context.save_traces = save_traces
    exit()
finally:
    _save_options_context.save_traces = previous_value
