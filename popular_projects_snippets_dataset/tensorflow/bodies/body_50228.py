# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Removes tracked references that are only used when loading the model."""
# Now that the node object has been fully loaded, and the checkpoint has
# been restored, the object no longer needs to track objects added from
# SerializedAttributes. (Note that saving a training checkpoint still
# functions correctly, because layers and variables are tracked separately
# by the Layer object.)
# TODO(kathywu): Instead of outright deleting these nodes (which would
# make restoring from a different checkpoint tricky), mark them as extra
# dependencies that are OK to overwrite.
for node in self.loaded_nodes.values():
    node = node[0]
    if not isinstance(node, base_layer.Layer):
        # Loaded nodes can contain other trackable objects created when
        # loading layers from the config, such as variables.
        continue
    for name in PUBLIC_ATTRIBUTES:
        node._delete_tracking(name)  # pylint: disable=protected-access

    if isinstance(node, functional_lib.Functional):
        # Delete the temporary layer dependencies, which were used to restore
        # the checkpointed values. When the model is live, the user can delete
        # or add layers to the model at any time, so these layer dependencies
        # may be obsolete.
        dependencies = list(node._self_unconditional_dependency_names)  # pylint: disable=protected-access
        for name in dependencies:
            if re.match(r'^layer(_with_weights)?-[\d+]', name) is not None:
                node._delete_tracking(name)  # pylint: disable=protected-access
