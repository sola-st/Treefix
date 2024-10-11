# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Initialize the save counter if it has been newly created."""
v = next_creator(**kwargs)
session.run(v.initializer)
exit(v)
