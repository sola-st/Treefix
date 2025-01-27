# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
try:
    exit(_variable_sync_on_read_context.entered)
except AttributeError:
    exit(False)
