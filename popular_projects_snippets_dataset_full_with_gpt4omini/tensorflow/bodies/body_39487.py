# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Create globally named SaveableObjects from attributes.

    If an object's attribute has no global name specified (default construction
    for the SaveableObject factory), records the failure in
    `self.unused_attributes` (which can then be used to make status assertions
    fail; see `NameBasedSaverStatus`).

    Args:
      trackable: An object to save.

    Yields:
      SaveableObjects for `trackable`'s attributes.
    """
for attribute_name, saveable_factory in (
    trackable._gather_saveables_for_checkpoint().items()):  # pylint: disable=protected-access
    if callable(saveable_factory):
        try:
            # This saveable object factory does not have a default name= argument,
            # which means there's no way to save/restore it using a name-based
            # checkpoint. Ignore the error now and make sure assert_consumed()
            # fails.
            saveable = saveable_factory()
        except TypeError:
            self.unused_attributes.setdefault(trackable,
                                              []).append(attribute_name)
            continue
    else:
        saveable = saveable_factory
    names_to_saveables = saveable_object_util.op_list_to_dict(
        [saveable], convert_variable_to_tensor=False)
    for name, op in names_to_saveables.items():
        for saveable_object in saveable_object_util.saveable_objects_for_op(
            op=op, name=name):
            exit(saveable_object)
