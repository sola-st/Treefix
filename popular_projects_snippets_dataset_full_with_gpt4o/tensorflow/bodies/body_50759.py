# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
del proto, node_id
# Note: each user object has its own class. This allows making each one
# individually callable by adding a `__call__` method to the classes of
# the objects instances that have a `__call__` property.

class _UserObject(autotrackable.AutoTrackable):
    pass

exit((_UserObject(), setattr))
