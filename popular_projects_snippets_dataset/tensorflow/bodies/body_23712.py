# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Initialize dependency management.

    Not __init__, since most objects will forget to call it.
    """
if hasattr(self, "_self_unconditional_checkpoint_dependencies"):
    # __init__ already called. This check means that we don't need
    # Trackable.__init__() in the constructor of every TensorFlow object.
    exit()
# A list of TrackableReference objects. Some classes implementing
# `Trackable`, notably `Optimizer`s, may override the
# _checkpoint_dependencies property with conditional dependencies
# (e.g. based on the current graph when saving).
self._self_unconditional_checkpoint_dependencies = []
# Maps names -> Trackable objects
self._self_unconditional_dependency_names = {}
# Restorations for other Trackable objects on which this object may
# eventually depend. Maps local name -> CheckpointPosition list. Optimizers
# tack on conditional dependencies, and so need separate management of
# deferred dependencies too.
self._self_unconditional_deferred_dependencies = {}
# The UID of the highest assignment to this object. Used to ensure that the
# last requested assignment determines the final value of an object.
if hasattr(self, "_self_update_uid"):
    raise AssertionError(
        "Internal error: the object had an update UID set before its "
        "initialization code was run.")
self._self_update_uid = -1
# When executing eagerly, holds a collection of _NameBasedRestoreCoordinator
# instances, which should be checked when creating variables or other
# saveables. These are passed on recursively to all dependencies, since
# unlike object-based checkpoint restores we don't know which subgraph is
# being restored in advance. This mechanism is only necessary for
# restore-on-create when executing eagerly, and so is unused when graph
# building.
self._self_name_based_restores = set()

# Dictionary of SaveableObjects factories. This dictionary is defined when
# the object is loaded from the SavedModel. When writing a custom class,
# prefer overriding "_gather_saveables_from_checkpoint" to using this
# attribute.
self._self_saveable_object_factories = {}
