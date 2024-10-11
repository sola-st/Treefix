# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Create distributed variables with given synchronization and aggregation."""
# Figure out what collections this variable should be added to.
# We'll add the MirroredVariable to those collections instead.
var_collections = kwargs.pop("collections", None)
if var_collections is None:
    var_collections = [ops.GraphKeys.GLOBAL_VARIABLES]
kwargs["collections"] = []

synchronization = _validate_synchronization(kwargs)
# Update synchronization in kwargs in case it's AUTO, which is converted to
# ON_WRITE.
kwargs["synchronization"] = synchronization
aggregation = _validate_aggregation(kwargs)
use_var_policy = getattr(strategy.extended, "_use_var_policy", False)

# Ignore user-specified caching device, not needed for mirrored variables.
kwargs.pop("caching_device", None)

# TODO(josh11b,apassos): It would be better if variable initialization
# was never recorded on the tape instead of having to do this manually
# here.
with tape.stop_recording():
    value_list = real_mirrored_creator(**kwargs)
    # MirroredVariable is recreated during saved_model loading, and its
    # component variables (value_list) will have None initializer. We
    # set their initializers to no_op so that consumer like
    # `global_variables_initializer` wouldn't complain, as it groups all
    # variables' initializers thus all variables have to have initializers.
    for v in value_list:
        # pylint:disable=protected-access
        if hasattr(v, "_initializer_op") and v._initializer_op is None:
            v._initializer_op = control_flow_ops.no_op()
        # pylint:enable=protected-access
    if use_var_policy:
        var_policy_cls = policy_mapping.get(synchronization)
        var_policy = var_policy_cls(aggregation=aggregation)
        var_cls = class_mapping.get("VariableClass")
        result = var_cls(strategy, value_list, aggregation, var_policy=var_policy)
    else:
        var_cls = class_mapping.get(synchronization)
        result = var_cls(strategy, value_list, aggregation)

  # Add the wrapped variable to the requested collections.
  # The handling of eager mode and the global step matches
  # ResourceVariable._init_from_args().
if not context.executing_eagerly():
    g = ops.get_default_graph()
    # If "trainable" is True, next_creator() will add the member variables
    # to the TRAINABLE_VARIABLES collection, so we manually remove
    # them and replace with the MirroredVariable. We can't set
    # "trainable" to False for next_creator() since that causes functions
    # like implicit_gradients to skip those variables.
    if kwargs.get("trainable", True):
        var_collections.append(ops.GraphKeys.TRAINABLE_VARIABLES)
        l = g.get_collection_ref(ops.GraphKeys.TRAINABLE_VARIABLES)
        for value in value_list:
            for i, trainable_variable in enumerate(l):
                if value is trainable_variable:
                    del l[i]
                    break

    g.add_to_collections(var_collections, result)
elif ops.GraphKeys.GLOBAL_STEP in var_collections:
    ops.add_to_collections(ops.GraphKeys.GLOBAL_STEP, result)

exit(result)
