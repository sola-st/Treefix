# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Generates all checkpoint save/restore functions.

    The save and restore functions are generated in the eager context (or in the
    user's Graph/Session) before being copied to the exported GraphDef. These
    functions record the ops for saving/restoring the entire object or
    individual objects (e.g. variables and hash tables).

    The global save and restore functions are generated for compatibility with
    TF1 and loading from C++, and is saved in the `MetaGraphDef.saver_def`.

    The individual functions are generated for the Python TF2 use case, where
    users use the loaded SavedModel as-is, or compose new models using parts
    of the object loaded from the SavedModel. These functions are recorded in
    the `saveable_objects` map in the `SavedObject` proto.
    """
checkpoint_factory_map, registered_savers = (
    save_util_v1.get_checkpoint_factories_and_keys(self.object_names))
self._obj_to_registered_saver = object_identity.ObjectIdentityDictionary()
for saver_name, trackables in registered_savers.items():
    for trackable in trackables.values():
        self._obj_to_registered_saver[trackable] = saver_name
self._saveable_objects_map = (
    _gen_save_and_restore_functions(checkpoint_factory_map))
