# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Returns the saveable generated from the factory method."""
matched_factory = None

# The `expected_factory_name` is used to find the right saveable factory,
# while the `factory_input_name` is the value that is passed to the factory
# method to instantiate the SaveableObject.
expected_factory_name = serialized_tensor.name
factory_input_name = serialized_tensor.checkpoint_key

# Case 1: the name already exactly matches a key in saveable_factories.
if expected_factory_name in saveable_factories:
    matched_factory = saveable_factories[expected_factory_name]

# Case 2: (Forward compat) The serialized name is composed of
# "factory_name" + "SUFFIX". Get the matching factory name.
if matched_factory is None:

    for factory_name, factory in saveable_factories.items():
        if expected_factory_name.startswith(factory_name):
            if matched_factory is not None:
                # This condition is met in the extreme edge case where the object
                # returns two saveable factories with similar names. This is very
                # unlikely because there zero objects inside TensorFlow that use
                # more than one saveable factory.
                raise ValueError("Forward compatibility load error: Unable to load "
                                 "checkpoint saved in future version of TensorFlow. "
                                 "Please update your version of TensorFlow to the "
                                 "version in which the checkpoint was saved.")

            matched_factory = factory
            factory_input_name = _extract_saveable_name(
                serialized_tensor.checkpoint_key) + factory_name
            created_compat_names.add(factory_name)

if callable(matched_factory):
    exit(matched_factory(name=factory_input_name))
exit(matched_factory)
