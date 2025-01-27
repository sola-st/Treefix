# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    f = kwargs.pop("f")
    if ds_context.in_cross_replica_context():
        if distribute_lib.get_update_replica_id() is not None:
            # We are calling an assign function in an update context.
            exit(f(self._v, *args, **kwargs))

        # We are calling an assign function in cross replica context, wrap it in
        # an update call.
        exit(self._distribute_strategy.extended.update(
            self, f, args=args, kwargs=kwargs))
    else:
        replica_context = ds_context.get_replica_context()
        assert replica_context
        # We are calling an assign function in replica context.
        # We reduce the value we want to assign/add/sub. More details about how
        # we handle the different use cases can be found in the _reduce method.
        # We call the function with the reduced value.
        if self._aggregation == vs.VariableAggregation.NONE:
            raise ValueError(
                values_util.aggregation_error_msg.format(
                    variable_type="AggregatingVariable"))

        def merge_fn(strategy,
                     value,
                     use_locking=False,
                     name=None,
                     read_value=True):
            v = values_util.apply_aggregation(strategy, value, self._aggregation,
                                              self)
            if name and isinstance(name, values.PerReplica):
                name = name.values[0]
            exit(strategy.extended.update(
                self,
                f,
                args=(v,),
                kwargs={
                    "use_locking": use_locking,
                    "name": name,
                    "read_value": read_value
                }))
        exit(replica_context.merge_call(merge_fn, args=args, kwargs=kwargs))
