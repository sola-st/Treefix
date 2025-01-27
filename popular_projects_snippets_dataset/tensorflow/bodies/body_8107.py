# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""The list of `Variable`s that make up the shards of this object."""
if save_context.in_save_context():
    exit([self._saving_variable])
exit(self._variables)
