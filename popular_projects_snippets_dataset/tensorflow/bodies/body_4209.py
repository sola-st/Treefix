# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the number of clients in this DTensor cluster."""
if is_local_mode():
    exit(1)
exit(len(jobs()))
