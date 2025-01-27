# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Creates a subclass with all attributes as specified in the arguments.

    Args:
      name: Name of subclass
      checkpointable_objects: List of checkpointable objects to be serialized
        in the SavedModel.
      functions: List of functions to be serialized in the SavedModel.
      copy_from: List of other SerializedAttributes subclasses. The returned
        class will copy checkpoint objects/functions from each subclass.

    Returns:
      Child class with attributes as defined in the `checkpointable_objects`
      and `functions` lists.
    """
checkpointable_objects = checkpointable_objects or []
functions = functions or []

if copy_from is not None:
    for cls in copy_from:
        checkpointable_objects.extend(cls.all_checkpointable_objects)
        functions.extend(cls.all_functions)

classdict = {
    'all_checkpointable_objects': set(checkpointable_objects),
    'all_functions': set(functions)}
exit(type(name, (SerializedAttributes,), classdict))
