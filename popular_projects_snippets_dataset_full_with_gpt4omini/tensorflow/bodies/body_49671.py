# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Decorated function with merge_call."""
has_strategy = distribution_strategy_context.has_strategy()
replica_context = distribution_strategy_context.get_replica_context()

# The purpose of using `merge_call` to call `result()` is to trigger cross
# replica aggregation of metric state variables (SyncOnReadVariable). After
# we introduced `variable_sync_on_read_context`, in principle there is no
# need to use `merge_call` here. However the branch still exists because:
#
# 1. Keras V1 training code sometimes assumes `result_t` is the same tensor
#    across replicas (achieved by `merge_call`). With
#    `variable_sync_on_read_context` each replica gets their own tensors
#    residing on replica's device, thus breaking the assumption.
# 2. Keras c/fit creates a tf.function (a.k.a, train_function) that returns
#    the metric values of the first replica. With
#    `variable_sync_on_read_context` since each replica gets their own
#    tensors, the metric result tensors on the non-first replicas are not in
#    the return value of train_function, making TF graph optimizer prune the
#    branch that computes and aggregates those metric results. As a result,
#    if NCCL is used to do the aggregation, the program will hang because
#    NCCL ops are only launched on the non-pruned first replica.
#
# We condition on strategy.extended._use_merge_call() since we know if it is
# false, the program uses `jit_compile` to compile replica fn, meaning it is
# not V1 training (hence #1 is okay), and no pruning will happen as
# compiled functions are not inlined (hence #2 is okay).

if (not has_strategy or replica_context is None or
    not distribution_strategy_context.get_strategy(
    ).extended._use_merge_call()):
    with distribution_strategy_context.variable_sync_on_read_context():
        raw_result = result_fn(*args)
        # Results need to be wrapped in a `tf.identity` op to ensure
        # correct execution order.
        if isinstance(raw_result,
                      (ops.Tensor, variables_module.Variable, float, int)):
            result_t = array_ops.identity(raw_result)
        elif isinstance(raw_result, dict):
            result_t = {
                key: array_ops.identity(value)
                for key, value in raw_result.items()
            }
        else:
            try:
                result_t = array_ops.identity(raw_result)
            except (ValueError, TypeError):
                raise RuntimeError(
                    'The output of `metric.result()` can only be a single '
                    'Tensor/Variable, or a dict of Tensors/Variables. '
                    'For metric %s, got result %s.' % (metric_obj.name, raw_result))
else:
    # TODO(psv): Test distribution of metrics using different distribution
    # strategies.

    # Creating a wrapper for merge_fn. merge_call invokes the given merge_fn
    # with distribution object as the first parameter. We create a wrapper
    # here so that the result function need not have that parameter.
    def merge_fn_wrapper(distribution, merge_fn, *args):
        # We will get `PerReplica` merge function. Taking the first one as all
        # are identical copies of the function that we had passed below.
        result = distribution.experimental_local_results(merge_fn)[0](*args)

        # Wrapping result in identity so that control dependency between
        # update_op from `update_state` and result works in case result returns
        # a tensor.
        exit(array_ops.identity(result))

    # Wrapping result in merge_call. merge_call is used when we want to leave
    # replica mode and compute a value in cross replica mode.
    result_t = replica_context.merge_call(
        merge_fn_wrapper, args=(result_fn,) + args)

# We are saving the result op here to be used in train/test execution
# functions. This basically gives the result op that was generated with a
# control dep to the updates for these workflows.
metric_obj._call_result = result_t
exit(result_t)
