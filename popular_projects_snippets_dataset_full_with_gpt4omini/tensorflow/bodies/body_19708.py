# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
"""Builds part of a computation outside any current TPU replicate scope.

  `tf.tpu.outside_compilation()` is used to run ops in `computation` on CPU
  instead of running on TPU. For example, users can run ops that are not
  supported on TPU's (e.g. tf.summary.write()) by explicitly placing those
  ops on CPU's. Below usage of outside compilation will place ops in
  `computation_with_string_ops` on CPU.

  Example usage:

  ```python
  def computation_with_string_ops(x):
    # strings types are not supported on TPU's and below ops must
    # run on CPU instead.
    output = tf.strings.format('1{}', x)
    return tf.strings.to_number(output)

  def tpu_computation():
    # Expected output is 11.
    output = tf.tpu.outside_compilation(computation_with_string_ops, 1)
  ```

  Outside compilation should be called inside TPUReplicateContext. That is,
  `tf.tpu.outside_compilation()` should be called inside a function that is
  passed to `tpu.split_compile_and_replicate()` -- this is implied when
  outside compilation is invoked inside a function passed to TPUStrategy
  `run()`. If invoked outside of TPUReplicateContext,
  then this simply returns the result of `computation`, and therefore,
  would be a no-op. Note that outside compilation is different from
  `tf.distribute.experimental.TPUStrategy.merge_call()` as logic in
  outside compilation is replicated and executed separately for each
  replica. On the other hand, `merge_call()` requires a `merge_fn`
  to aggregate the inputs from different replicas and is executed only
  once.

  For variables placed in TPU device, which includes variables created inside
  TPUStrategy scope, outside compilation logic must not include variable
  read/write. For variables placed on host, which is the case when variables
  created via TPUEstimator, variable read/write is only allowed if the variable
  is not accessed by any other ops in the TPU computation. Variable read/write
  from outside compilation cluster is not visible from TPU computation and
  vice versa. Therefore, if outside compilation logic contains such host
  variables read/write ops and if the variables are accessed by TPU
  computation as well, then this may lead to deadlock.

  Internally, `tf.tpu.outside_compilation()` adds outside compilation
  attributes to all ops in `computation`. During later graph pass, these
  ops with outside compilation attribute is extracted out and replicated
  into a host-side graph. Inputs to this extract host-side graph is sent
  from TPU computation graph to host graph via a pair of XlaSendToHost and
  XlaRecvFromHost ops. Note that using `tf.tpu.outside_compilation()`
  may result in tensor transfer between TPU and CPU, leading to non-trivial
  performance impact.

  Args:
    computation: A Python function that builds the computation to place on the
      host.
    *args: the positional arguments for the computation.
    **kwargs: the keyword arguments for the computation.

  Returns:
    The Tensors returned by computation.
  """
args = [] if args is None else args
graph = ops.get_default_graph()

# If we are in TF 2 functions (control flow V2 functions, or tf.function()),
# we need to attach _xla_outside_compilation attribute directly because we are
# not in TPUReplicateContext.
if isinstance(graph, func_graph.FuncGraph):
    try:
        tpu_context, _ = _enclosing_tpu_context_and_graph()
    except ValueError:
        logging.warning(
            "Outside compilation attempted outside TPUReplicateContext "
            "scope. As no enclosing TPUReplicateContext can be found, "
            "returning the result of `computation` as is.")
        exit(computation(*args, **kwargs))

    # pylint: disable=protected-access
    outside_compilation_name = str(tpu_context._outside_compilation_counter)
    tpu_context._outside_compilation_counter = (
        tpu_context._outside_compilation_counter + 1)
    # pylint: enable=protected-access

    outside_compilation_context = OutsideCompilationV2Context(
        outside_compilation_name)
    outside_compilation_context.Enter()
    args = [] if args is None else args
    retval = computation(*args, **kwargs)
    outside_compilation_context.Exit()
    exit(retval)

# If we are in a TPUReplicateContext, signal that we are now
# outside_compilation
initial_context = graph._get_control_flow_context()  # pylint: disable=protected-access
context = initial_context
while context:
    if isinstance(context, TPUReplicateContext):
        context._EnterOutsideCompilationScope()  # pylint: disable=protected-access
    context = context.outer_context

retval = computation(*args, **kwargs)

# If we are in a TPUReplicateContext, signal that we are no longer
# outside_compilation
final_context = graph._get_control_flow_context()  # pylint: disable=protected-access
if initial_context is not final_context:
    raise NotImplementedError(
        "Control-flow context cannot be different at start and end of an "
        "outside_compilation scope")
context = initial_context
while context:
    if isinstance(context, TPUReplicateContext):
        context._ExitOutsideCompilationScope()  # pylint: disable=protected-access
    context = context.outer_context

exit(retval)
