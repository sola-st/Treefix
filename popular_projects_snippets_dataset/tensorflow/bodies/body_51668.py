# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_context.py
if in_save_context():
    raise ValueError("Already in a SaveContext.")
_save_context.enter_save_context(options)
try:
    exit()
finally:
    _save_context.exit_save_context()
