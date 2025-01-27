# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
"""`merge_call()` implementation for synchronized replica.

    This pauses the current replica thread and passes `fn` and its arguments to
    the main thread. The main thread will wait until all replicas pause, then
    invoke `fn` with grouped arguments. The current replica thread will continue
    after `fn` completes.

    See `_call_for_each_replica` for the logic in the main thread.

    Args:
      fn: a function that is called in cross replica context with grouped
        arguments from each replica. `fn` should returns grouped values.
      args: positional arguments to `fn`.
      kwargs: keyward arguments to `fn`.

    Returns:
      Return value of `fn` for the current replica.

    Raises:
      RuntimeError: when merge_call happens in a different graph, e.g. in a
        different tf.function, which is not supported now.
      _RequestedStop: when stop is requested.

    """
t = threading.current_thread()
assert isinstance(t, _MirroredReplicaThread)
t.merge_fn = fn
t.merge_args = args
t.merge_kwargs = kwargs
t.captured_name_scope = t.graph.get_name_scope()
# Adding a "/" at end lets us re-enter this scope later.
if t.captured_name_scope:
    t.captured_name_scope += "/"

t.captured_var_scope = variable_scope.get_variable_scope()
t.captured_control_deps = t.graph._current_control_dependencies()  # pylint: disable=protected-access

t.merge_call_entered_in_eager = context.context().executing_eagerly()

# It is problematic if `merge_call` is called under a different graph other
# than the one that `_call_for_each_replica` is called under, there are
# 3 cases this can happen:
#
#   1. The `fn` passed to `_call_for_each_replica` is decorated with
#   `tf.function` and there is a `merge_call` in `fn`. Since
#   MirroredStrategy traces a separate function per thread (per device),
#   and each trace takes a shared lock, the lock is never released by the
#   first thread and subsequent replica threads cannot proceed to trace
#   their own functions. This issue is addressed by always converting
#   `_call_for_each_replica(tf.function(f))` to
#   ``tf.function(_call_for_each_replica(f))`.` in
#   `MirroredStrategy._call_for_each_replica`.
#
#   2. The `fn` passed to `_call_for_each_replica` contains a nested
#   `tf.function`, and there is a `merge_call` in the nested `tf.function`.
#   In this case each thread can successfully trace its own function, but
#   since the `merge_fn` passed to `merge_call` is executed in the main
#   thread (where `_call_for_each_replica` is executed), it can't access
#   the tensors that come from different graphs.
#
#   3. The `fn` passed to `_call_for_each_replica` contains a control-flow
#   statement, and there is a `merge_call` inside the control-flow body,
#   `fn` or `_call_for_each_replica` is decorated with `tf.function`.
#   Control flow statement creates a separate graph for its body, similar
#   to #2, `merge_fn` executed in the main thread can't access the
#   tensors that come from different graphs.
#
#   We raise an error for #2 and #3.
if ops.get_default_graph() != t.graph:
    raise RuntimeError(
        "`merge_call` called while defining a new graph or a tf.function."
        " This can often happen if the function `fn` passed to"
        " `strategy.run()` contains a nested `@tf.function`, and the nested "
        "`@tf.function` contains a synchronization point, such as aggregating"
        " gradients (e.g, optimizer.apply_gradients), or if the function `fn`"
        " uses a control flow statement which contains a synchronization"
        " point in the body. Such behaviors are not yet supported. Instead,"
        " please avoid nested `tf.function`s or control flow statements that"
        " may potentially cross a synchronization boundary, for example,"
        " wrap the `fn` passed to `strategy.run` or the entire `strategy.run`"
        " inside a `tf.function` or move the control flow out of `fn`. If"
        " you are subclassing a `tf.keras.Model`, please avoid decorating"
        " overridden methods `test_step` and `train_step` in `tf.function`.")

t.has_paused.set()
t.should_run.wait()
t.should_run.clear()
if t.coord.should_stop():
    raise _RequestedStop()
t.merge_call_entered_in_eager = None
exit(t.merge_result)
