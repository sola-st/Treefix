# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
"""Run `fn` in separate threads, once per replica/worker device.

  Args:
    distribution: the DistributionStrategy object.
    fn: function to run (will be run once per replica, each in its own thread).
    args: positional arguments for `fn`
    kwargs: keyword arguments for `fn`.

  Returns:
    Merged return value of `fn` across all replicas.

  Raises:
    RuntimeError: If fn() calls get_replica_context().merge_call() a different
        number of times from the available devices.
  """
# TODO(josh11b): Add this option once we add synchronization to variable
# creation. Until then, this is pretty unsafe to use.
run_concurrently = False
if not context.executing_eagerly():
    # Needed for per-thread device, etc. contexts in graph mode.
    ops.get_default_graph().switch_to_thread_local()

coord = coordinator.Coordinator(clean_stop_exception_types=(_RequestedStop,))

shared_variable_store = {}
devices = distribution.extended.worker_devices

thread_local_callables = _get_thread_local_configuration_callable()

# TODO(isaprykin): Create these threads once instead of during every call.
threads = []
for index in range(len(devices)):
    variable_creator_fn = shared_variable_creator.make_fn(
        shared_variable_store, index)
    t = _MirroredReplicaThread(distribution, coord, index, devices,
                               variable_creator_fn, fn,
                               distribute_utils.caching_scope_local,
                               distribute_utils.select_replica(index, args),
                               distribute_utils.select_replica(index, kwargs),
                               thread_local_callables)
    threads.append(t)

for t in threads:
    t.start()

# When `fn` starts `should_run` event is set on _MirroredReplicaThread
# (`MRT`) threads. The execution waits until
# `MRT.has_paused` is set, which indicates that either `fn` is
# complete or a `get_replica_context().merge_call()` is called.  If `fn` is
# complete, then `MRT.done` is set to True.  Otherwise, arguments
# of `get_replica_context().merge_call` from all paused threads are grouped
# and the `merge_fn` is performed.  Results of the
# `get_replica_context().merge_call` are then set to `MRT.merge_result`.
# Each such `get_replica_context().merge_call` call returns the
# `MRT.merge_result` for that thread when `MRT.should_run` event
# is reset again. Execution of `fn` resumes.

try:
    with coord.stop_on_exception():
        all_done = False
        while not all_done and not coord.should_stop():
            done = []
            if run_concurrently:
                for t in threads:
                    t.should_run.set()
                for t in threads:
                    t.has_paused.wait()
                    t.has_paused.clear()
                    if coord.should_stop():
                        exit(None)
                    done.append(t.done)
            else:
                for t in threads:
                    t.should_run.set()
                    t.has_paused.wait()
                    t.has_paused.clear()
                    if coord.should_stop():
                        exit(None)
                    done.append(t.done)
            if coord.should_stop():
                exit(None)
            all_done = all(done)
            if not all_done:
                if any(done):
                    raise RuntimeError("Some replicas made a different number of "
                                       "replica_context().merge_call() calls.")
                # get_replica_context().merge_call() case
                merge_args = distribute_utils.regroup(
                    tuple(t.merge_args for t in threads))
                merge_kwargs = distribute_utils.regroup(
                    tuple(t.merge_kwargs for t in threads))
                # We capture the name_scope of the MRT when we call merge_fn
                # to ensure that if we have opened a name scope in the MRT,
                # it will be respected when executing the merge function. We only
                # capture the name_scope from the first MRT and assume it is
                # the same for all other MRTs.
                mtt_captured_name_scope = threads[0].captured_name_scope
                mtt_captured_var_scope = threads[0].captured_var_scope
                # Capture and merge the control dependencies from all the threads.
                mtt_captured_control_deps = set()
                for t in threads:
                    mtt_captured_control_deps.update(t.captured_control_deps)

                # Control is transfered from _MirroredReplicaThread (MRT) to the main
                # thread, i.e., here, to perform `merge_fn`, and thus we preserve the
                # name scope,  control dependencies, etc. from MRT at the time
                # `merge_call` is made.
                # One special case is that the `merge_call` is made under an
                # `tf.init_scope` in the MRT. `tf.init_scope` will clear control
                # dependencies, pause gradient tape, and enter the lowest context on
                # the `context_stack` that is not building a graph function. Entering
                # the lowest context could be one of the two things: installation of a
                # graph as the default graph or switch into eager mode. If the former
                # is done and causes `merge_call` to be called in a different graph
                # from the one in which `call_for_each_replica` is called, we do not
                # allow this case (see comment in `_merge_call`) and we would not have
                # arrived here due to the assertion in `_merge_call`. However, if the
                # latter is done, we want to make sure the main thread enter an eager
                # mode scope as well so that `merge_fn` does not have trouble
                # accessing resources defined in MRT under the same context.
                with ops.name_scope(
                    mtt_captured_name_scope), ops.control_dependencies(
                        mtt_captured_control_deps), variable_scope.variable_scope(
                            mtt_captured_var_scope), _maybe_enter_eager_mode(
                                threads[0].merge_call_entered_in_eager):
                    merge_result = threads[0].merge_fn(distribution, *merge_args,
                                                       **merge_kwargs)
                for r, t in enumerate(threads):
                    t.merge_result = distribute_utils.select_replica(r, merge_result)
finally:
    for t in threads:
        t.should_run.set()
    coord.join(threads)

exit(distribute_utils.regroup(tuple(t.main_result for t in threads)))
