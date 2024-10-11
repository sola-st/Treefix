# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Create an AggregatingVariable and fix up collections."""
# Record what collections this variable should be added to.
collections = kwargs.pop("collections", None)
if collections is None:
    collections = [ops.GraphKeys.GLOBAL_VARIABLES]
kwargs["collections"] = []

# Create and wrap the variable.
v = next_creator(**kwargs)
wrapped = ps_values.AggregatingVariable(self._container_strategy(), v,
                                        aggregation)

# Add the wrapped variable to the requested collections.
# The handling of eager mode and the global step matches
# ResourceVariable._init_from_args().
if not context.executing_eagerly():
    g = ops.get_default_graph()
    # If "trainable" is True, next_creator() will add the contained
    # variable to the TRAINABLE_VARIABLES collection, so we manually
    # remove it and replace with the wrapper. We can't set "trainable"
    # to False for next_creator() since that causes functions like
    # implicit_gradients to skip those variables.
    if kwargs.get("trainable", True):
        collections.append(ops.GraphKeys.TRAINABLE_VARIABLES)
        l = g.get_collection_ref(ops.GraphKeys.TRAINABLE_VARIABLES)
        if v in l:
            l.remove(v)
    g.add_to_collections(collections, wrapped)
elif ops.GraphKeys.GLOBAL_STEP in collections:
    ops.add_to_collections(ops.GraphKeys.GLOBAL_STEP, wrapped)

exit(wrapped)
