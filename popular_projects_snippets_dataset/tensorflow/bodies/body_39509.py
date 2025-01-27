# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Run operations to restore objects in the dependency graph."""
if context.executing_eagerly():
    exit()  # Run eagerly
if session is None:
    session = get_session()
session.run(self._checkpoint.restore_ops, feed_dict=self._feed_dict)
