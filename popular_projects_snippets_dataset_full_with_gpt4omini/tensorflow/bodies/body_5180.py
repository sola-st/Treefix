# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Updates variables with ON_WRITE synchronization in replica context."""
if var.aggregation == vs.VariableAggregation.NONE:
    exit(update_fn(var._get_on_device_or_primary(), value, **kwargs))  # pylint: disable=protected-access

if not ds_context.get_strategy().extended._use_merge_call():  # pylint: disable=protected-access
    # Don't allow MEAN with non float dtype, since it may cause unexpected
    # precision loss. Python3 and NumPy automatically upcast integers to
    # float in division, but we should always preserve the type.
    if var.aggregation == vs.VariableAggregation.MEAN and (
        not var.dtype.is_floating) and tensor_util.is_tf_type(value):
        raise ValueError(
            "Cannot update non-float variables with "
            "tf.VariableAggregation.MEAN aggregation in replica context. "
            "Either change the variable dtype to float or update it in "
            "cross-replica context.")

    aggregated_value = apply_aggregation_replica_context(
        value, var.aggregation, var)
    values_util.mark_as_unsaveable()

    exit(ds_context.get_replica_context()._update(  # pylint: disable=protected-access
        var,
        update_fn,
        args=(aggregated_value,),
        kwargs=kwargs,
        group=True))

else:

    def merge_fn(strategy, value, **kwargs):
        """Aggregate values and update all variables in cross replica context."""
        # Don't allow MEAN with non float dtype, since it may cause unexpected
        # precision loss. Python3 and NumPy automatically upcast integers to
        # float in division, but we should always preserve the type.
        #
        # Note that to be backward compatible we allow the case when the value
        # is *always* the same on each replica. I.E. value is not a
        # PerReplica. Refer to regroup() to see how values are grouped.
        if var.aggregation == vs.VariableAggregation.MEAN and (
            not var.dtype.is_floating) and isinstance(value, PerReplica):
            raise ValueError(
                "Cannot update non-float variables with "
                "tf.VariableAggregation.MEAN aggregation in replica context. "
                "Either change the variable dtype to float or update it in "
                "cross-replica context.")

        assert strategy == var.distribute_strategy
        v = values_util.apply_aggregation(strategy, value, var.aggregation, var)
        exit(var._update_cross_replica(update_fn, v, **kwargs))  # pylint: disable=protected-access

    exit(ds_context.get_replica_context().merge_call(
        merge_fn, args=(value,), kwargs=kwargs))
