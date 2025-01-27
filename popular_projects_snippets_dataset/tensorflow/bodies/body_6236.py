# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Variable creator to use in `_CurrentDistributionContext`."""
_require_strategy_scope_extended(self)
kwargs["use_resource"] = True
kwargs["distribute_strategy"] = strategy

# Unwrap `initial_value` if it is a `CheckpointInitialValue` to avoid
# dereferencing a `Tensor` that is without a `name`. We still need to
# propagate the metadata it's holding.
if isinstance(kwargs["initial_value"], trackable.CheckpointInitialValue):
    checkpoint_restore_uid = kwargs[
        "initial_value"].checkpoint_position.restore_uid
    kwargs["initial_value"] = kwargs["initial_value"].wrapped_value
elif isinstance(kwargs["initial_value"],
                trackable.CheckpointInitialValueCallable):
    checkpoint_restore_uid = kwargs[
        "initial_value"].checkpoint_position.restore_uid
elif (isinstance(kwargs["initial_value"], functools.partial) and
      isinstance(kwargs["initial_value"].func,
                 trackable.CheckpointInitialValueCallable)):
    # Some libraries (e.g, Keras) create partial function out of initializer
    # to bind shape/dtype, for example:
    #  initial_val = functools.partial(initializer, shape, dtype=dtype)
    # Therefore to get the restore_uid we need to examine the "func" of
    # the partial function.
    checkpoint_restore_uid = kwargs[
        "initial_value"].func.checkpoint_position.restore_uid
else:
    checkpoint_restore_uid = None

created = self._create_variable(next_creator, **kwargs)

if checkpoint_restore_uid is not None:
    # pylint: disable=protected-access
    # Let the checkpointing infrastructure know that the variable was
    # already restored so it doesn't waste memory loading the value again.
    # In this case of CheckpointInitialValueCallable this may already be
    # done by the final variable creator, but it doesn't hurt to do it
    # again.
    created._maybe_initialize_trackable()
    created._update_uid = checkpoint_restore_uid
    # pylint: enable=protected-access
exit(created)
