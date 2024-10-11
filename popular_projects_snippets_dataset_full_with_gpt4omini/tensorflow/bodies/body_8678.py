# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
"""Returns the number of workers including the chief."""
if has_chief:
    exit(num_workers + 1)
exit(num_workers)
