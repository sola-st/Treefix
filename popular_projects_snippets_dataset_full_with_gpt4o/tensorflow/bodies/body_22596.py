# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
"""Apply gradients to variables.

    This contains most of the synchronization implementation and also wraps the
    apply_gradients() from the real optimizer.

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        compute_gradients().
      global_step: Optional Variable to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the Optimizer constructor.

    Returns:
      train_op: The op to dequeue a token so the replicas can exit this batch
      and start the next one. This is executed by each replica.

    Raises:
      ValueError: If the grads_and_vars is empty.
      ValueError: If global step is not provided, the staleness cannot be
        checked.
    """
if not grads_and_vars:
    raise ValueError("Must supply at least one variable")

if global_step is None:
    raise ValueError("Global step is required to check staleness")

self._global_step = global_step
train_ops = []
aggregated_grad = []
var_list = []

# local_anchor op will be placed on this worker task by default.
local_anchor = control_flow_ops.no_op()
# Colocating local_step variable prevents it being placed on the PS.
distribution_strategy = distribution_strategy_context.get_strategy()
with distribution_strategy.extended.colocate_vars_with(local_anchor):
    self._local_step = variable_scope.variable(
        initial_value=0,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        dtype=global_step.dtype.base_dtype,
        name="sync_rep_local_step")

self.local_step_init_op = state_ops.assign(self._local_step, global_step)
chief_init_ops = [self.local_step_init_op]
self.ready_for_local_init_op = variables.report_uninitialized_variables(
    variables.global_variables())

with ops.name_scope(None, self._name):
    for grad, var in grads_and_vars:
        var_list.append(var)
        with ops.device(var.device):
            # Dense gradients.
            if grad is None:
                aggregated_grad.append(None)  # pass-through.
                continue
            elif isinstance(grad, ops.Tensor):
                grad_accum = data_flow_ops.ConditionalAccumulator(
                    grad.dtype,
                    shape=var.get_shape(),
                    shared_name=var.name + "/grad_accum")
                train_ops.append(grad_accum.apply_grad(
                    grad, local_step=self._local_step))
                aggregated_grad.append(grad_accum.take_grad(
                    self._replicas_to_aggregate))
            else:
                if not isinstance(grad, indexed_slices.IndexedSlices):
                    raise ValueError("Unknown grad type!")
                grad_accum = data_flow_ops.SparseConditionalAccumulator(
                    grad.dtype, shape=(), shared_name=var.name + "/grad_accum")
                train_ops.append(grad_accum.apply_indexed_slices_grad(
                    grad, local_step=self._local_step))
                aggregated_grad.append(grad_accum.take_indexed_slices_grad(
                    self._replicas_to_aggregate))

            self._accumulator_list.append((grad_accum, var.device))

    aggregated_grads_and_vars = zip(aggregated_grad, var_list)

    # sync_op will be assigned to the same device as the global step.
    with ops.device(global_step.device), ops.name_scope(""):
        update_op = self._opt.apply_gradients(aggregated_grads_and_vars,
                                              global_step)

    # Create token queue.
    with ops.device(global_step.device), ops.name_scope(""):
        sync_token_queue = (
            data_flow_ops.FIFOQueue(-1,
                                    global_step.dtype.base_dtype,
                                    shapes=(),
                                    name="sync_token_q",
                                    shared_name="sync_token_q"))
        self._sync_token_queue = sync_token_queue

    with ops.device(global_step.device), ops.name_scope(""):
        # Replicas have to wait until they can get a token from the token queue.
        with ops.control_dependencies(train_ops):
            token = sync_token_queue.dequeue()
        train_op = state_ops.assign(self._local_step, token)

        with ops.control_dependencies([update_op]):
            # Sync_op needs to insert tokens to the token queue at the end of the
            # step so the replicas can fetch them to start the next step.
            tokens = array_ops.fill([self._tokens_per_step], global_step)
            sync_op = sync_token_queue.enqueue_many((tokens,))

        if self._variable_averages is not None:
            with ops.control_dependencies([sync_op]), ops.name_scope(""):
                sync_op = self._variable_averages.apply(
                    self._variables_to_average)

        self._chief_queue_runner = queue_runner.QueueRunner(
            sync_token_queue, [sync_op])
    for accum, dev in self._accumulator_list:
        with ops.device(dev):
            chief_init_ops.append(
                accum.set_global_step(
                    global_step, name="SetGlobalStep"))
    self.chief_init_op = control_flow_ops.group(*(chief_init_ops))
    self._gradients_applied = True
    exit(train_op)
