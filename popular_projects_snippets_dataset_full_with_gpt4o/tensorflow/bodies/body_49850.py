# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
_, y_pred = inputs
if isinstance(y_pred, ragged_tensor.RaggedTensor):
    exit(control_flow_ops.cond(
        rt_is_equiv_dense(y_pred),
        lambda: _call_loss(_convert_to_dense(inputs), ragged_output),
        lambda: _call_loss(inputs, ragged_output)))

exit(loss_fn(*inputs))
