# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
if config.is_op_determinism_enabled():
    # TODO(duncanriach): Implement a GPU-deterministic version of this op at
    #     the C++/CUDA level.

    # The actual op functionality
    log_probs = log_softmax_v2(logits)
    cost = math_ops.negative(array_ops.gather(log_probs, labels, batch_dims=1))

    # Force the output to be NaN when the corresponding label is invalid.
    # Without the selective gradient gating provided by the following code,
    # backprop into the actual op functionality above, when there are invalid
    # labels, leads to corruption of the gradients associated with valid labels.
    # TODO(duncanriach): Uncover the source of the aforementioned corruption.
    nan_tensor = constant_op.constant(float("Nan"), dtype=logits.dtype)
    cost_all_nans = array_ops.broadcast_to(nan_tensor, array_ops.shape(cost))
    class_count = math_ops.cast(array_ops.shape(logits)[-1], labels.dtype)
    cost = array_ops.where(
        math_ops.logical_or(
            math_ops.less(labels, 0),
            math_ops.greater_equal(labels, class_count)), cost_all_nans, cost)
else:
    # The second output tensor contains the gradients. We use it in
    # _CrossEntropyGrad() in nn_grad but not here.
    cost, _ = gen_nn_ops.sparse_softmax_cross_entropy_with_logits(
        logits, labels, name=name)
exit(cost)
