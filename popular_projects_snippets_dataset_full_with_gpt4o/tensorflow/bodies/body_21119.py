# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Create a scaffold.

    Args:
      init_op: Optional op for initializing variables.
      init_feed_dict: Optional session feed dictionary to use when running the
        init_op.
      init_fn: Optional function to use to initialize the model after running
        the init_op.  Will be called as `init_fn(scaffold, session)`.
      ready_op: Optional op to verify that the variables are initialized.  Must
        return an empty 1D string tensor when the variables are initialized, or
        a non-empty 1D string tensor listing the names of the non-initialized
        variables.
      ready_for_local_init_op: Optional op to verify that the global variables
        are initialized and `local_init_op` can be run. Must return an empty 1D
        string tensor when the global variables are initialized, or a non-empty
        1D string tensor listing the names of the non-initialized global
        variables.
      local_init_op: Optional op to initialize local variables.
      summary_op: Optional op to gather all summaries.  Must return a scalar
        string tensor containing a serialized `Summary` proto.
      saver: Optional `tf.compat.v1.train.Saver` object to use to save and
        restore variables.  May also be a `tf.train.Checkpoint` object, in which
        case object-based checkpoints are saved. This will also load some
        object-based checkpoints saved from elsewhere, but that loading may be
        fragile since it uses fixed keys rather than performing a full
        graph-based match. For example if a variable has two paths from the
        `Checkpoint` object because two `Model` objects share the `Layer` object
        that owns it, removing one `Model` may change the keys and break
        checkpoint loading through this API, whereas a graph-based match would
        match the variable through the other `Model`.
      copy_from_scaffold: Optional scaffold object to copy fields from. Its
        fields will be overwritten by the provided fields in this function.
      local_init_feed_dict: Optional session feed dictionary to use when running
        the local_init_op.
    """
if copy_from_scaffold is not None:
    if not isinstance(copy_from_scaffold, Scaffold):
        raise TypeError('copy_from_scaffold is not a Scaffold instance.')
    # We need _coalesce since Tensor is not converted to bool automatically,
    # so the common idiom of (a or b) does not work.
    coalesce = lambda a, b: a if a is not None else b
    init_op = coalesce(init_op, copy_from_scaffold.init_op)
    init_feed_dict = coalesce(init_feed_dict,
                              copy_from_scaffold.init_feed_dict)
    # Use the original init_fn provided by the user to init the new Scaffold.
    init_fn = coalesce(init_fn, copy_from_scaffold._user_init_fn)  # pylint: disable=protected-access
    ready_op = coalesce(ready_op, copy_from_scaffold.ready_op)
    ready_for_local_init_op = coalesce(
        ready_for_local_init_op, copy_from_scaffold.ready_for_local_init_op)
    local_init_op = coalesce(local_init_op, copy_from_scaffold.local_init_op)
    local_init_feed_dict = coalesce(local_init_feed_dict,
                                    copy_from_scaffold.local_init_feed_dict)
    summary_op = coalesce(summary_op, copy_from_scaffold.summary_op)
    saver = coalesce(saver, copy_from_scaffold.saver)

# NOTE(touts): modifying the init function to be passed the scaffold is a
# hack to make it easy to find the saver.  Is there a better way?
self._user_init_fn = init_fn
if init_fn:
    self._init_fn = lambda sess: init_fn(self, sess)
else:
    self._init_fn = None

self._init_op = init_op
self._init_feed_dict = init_feed_dict
self._ready_op = ready_op
self._ready_for_local_init_op = ready_for_local_init_op
self._local_init_op = local_init_op
self._local_init_feed_dict = local_init_feed_dict
self._summary_op = summary_op
self._saver = saver
