# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Get the aggregated gradients for op.

  Args:
    grads: The map of memoized gradients.
    op: The op to get gradients for.
    gradient_uid: A unique identifier within the graph indicating
      which invocation of gradients is being executed. Used to cluster
      ops for compilation.
    loop_state: An object for maintaining the state of the while loops in the
                graph. It is of type ControlFlowState. None if the graph
                contains no while loops.
    aggregation_method: Specifies the method used to combine gradient terms.
      Accepted values are constants defined in the class `AggregationMethod`.

  Returns:
    A list of gradients, one per each output of `op`. If the gradients
      for a particular output is a list, this function aggregates it
      before returning.

  Raises:
    TypeError: if the incoming grads are not Tensors or IndexedSlices.
    ValueError: if the arguments are invalid.

  """
if aggregation_method is None:
    aggregation_method = AggregationMethod.DEFAULT
valid_aggregation_methods = [
    AggregationMethod.ADD_N, AggregationMethod.EXPERIMENTAL_TREE,
    AggregationMethod.EXPERIMENTAL_ACCUMULATE_N]
if aggregation_method not in valid_aggregation_methods:
    raise ValueError(
        f"Invalid `aggregation_method` specified {aggregation_method}. "
        f"Accepted values are {valid_aggregation_methods}.")
out_grads = _GetGrads(grads, op)
for i, out_grad in enumerate(out_grads):
    if loop_state:
        if isinstance(out_grad, (ops.Tensor, indexed_slices.IndexedSlices)):
            assert control_flow_util.IsLoopSwitch(op)
            continue
    # Grads have to be Tensors or IndexedSlices
    if (isinstance(out_grad, collections_abc.Sequence) and not all(
        isinstance(g, (ops.Tensor, indexed_slices.IndexedSlices))
        for g in out_grad
        if g is not None)):
        raise TypeError(f"Invalid gradient {out_grad} [index = {i}]. Gradients "
                        "have to be either all Tensors or all IndexedSlices")
    # Aggregate multiple gradients, and convert [] to None.
    if out_grad:
        if len(out_grad) < 2:
            used = "nop"
            out_grads[i] = out_grad[0]
        elif all(isinstance(g, ops.Tensor) for g in out_grad if g is not None):
            tensor_shape = _AccumulatorShape(out_grad)
            if aggregation_method in [
                AggregationMethod.EXPERIMENTAL_TREE,
                AggregationMethod.EXPERIMENTAL_ACCUMULATE_N
            ]:
                # Aggregate all gradients by doing pairwise sums: this may
                # reduce performance, but it can improve memory because the
                # gradients can be released earlier.
                #
                # TODO(vrv): Consider replacing this with a version of
                # tf.AddN() that eagerly frees its inputs as soon as they are
                # ready, so the order of this tree does not become a problem.
                used = "tree"
                with ops.name_scope(op.name + "_gradient_sum"):
                    running_sum = out_grad[0]
                    for grad in out_grad[1:]:
                        running_sum = math_ops.add_n([running_sum, grad])
                    out_grads[i] = running_sum
            else:
                used = "add_n"
                out_grads[i] = _MultiDeviceAddN(out_grad, gradient_uid)
            logging.vlog(2, "  _AggregatedGrads %d x %s using %s", len(out_grad),
                         tensor_shape, used)
        else:
            out_grads[i] = backprop_util.AggregateIndexedSlicesGradients(out_grad)  # pylint: disable=protected-access
    else:  # not out_grad
        # out_grads[i] is [], thus its aggregation is simply None.
        out_grads[i] = None
exit(out_grads)
