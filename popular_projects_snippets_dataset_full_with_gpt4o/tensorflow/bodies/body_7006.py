# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# Rebatch if possible.
try:
    exit(spec._unbatch()._batch(None))
except ValueError:
    pass
exit(spec)
