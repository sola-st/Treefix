# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
"""Creates a _TreeEnsembleSavable object.

    Args:
      resource_handle: handle to the decision tree ensemble variable.
      create_op: the op to initialize the variable.
      name: the name to save the tree ensemble variable under.
    """
stamp_token, serialized = (
    gen_boosted_trees_ops.boosted_trees_serialize_ensemble(resource_handle))
# slice_spec is useful for saving a slice from a variable.
# It's not meaningful the tree ensemble variable. So we just pass an empty
# value.
slice_spec = ''
specs = [
    saver.BaseSaverBuilder.SaveSpec(stamp_token, slice_spec,
                                    name + '_stamp'),
    saver.BaseSaverBuilder.SaveSpec(serialized, slice_spec,
                                    name + '_serialized'),
]
super(_TreeEnsembleSavable, self).__init__(resource_handle, specs, name)
self.resource_handle = resource_handle
self._create_op = create_op
