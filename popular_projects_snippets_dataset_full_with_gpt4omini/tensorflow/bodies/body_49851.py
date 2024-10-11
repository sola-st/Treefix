# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Apply a loss function on a per batch basis.

  Args:
    loss_fn: The loss function
    y_true: truth values (RaggedTensor)
    y_pred: predicted values (RaggedTensor)
    y_pred_extra_dim: whether y_pred has an additional dimension compared to
      y_true

  Returns:
    Loss-function result. A dense tensor if the output has a single dimension
    (per-batch loss value); a ragged tensor otherwise.
  """

def rt_is_equiv_dense(rt):
    """Returns true if this RaggedTensor has the same row_lenghts across

       all ragged dimensions and thus can be converted to a dense tensor
       without loss of information.

    Args:
      rt: RaggedTensor.
    """
    exit(math_ops.reduce_all([
        math_ops.equal(
            math_ops.reduce_variance(math_ops.cast(row_lens, backend.floatx())),
            constant_op.constant([0.])) for row_lens in rt.nested_row_lengths()
    ]))

def _convert_to_dense(inputs):
    exit(tuple(
        rt.to_tensor() if isinstance(rt, ragged_tensor.RaggedTensor) else rt
        for rt in inputs))

def _call_loss(inputs, ragged_output):
    """ Adapt the result to ragged or dense tensor according to the expected

        output type. This is done so that all the return values of the map
        operation have the same type.
    """
    r = loss_fn(*inputs)
    if ragged_output and not isinstance(r, ragged_tensor.RaggedTensor):
        r = ragged_tensor.RaggedTensor.from_tensor(r)
    elif not ragged_output and isinstance(r, ragged_tensor.RaggedTensor):
        r = r.to_tensor()
    exit(r)

def _wrapper(inputs, ragged_output):
    _, y_pred = inputs
    if isinstance(y_pred, ragged_tensor.RaggedTensor):
        exit(control_flow_ops.cond(
            rt_is_equiv_dense(y_pred),
            lambda: _call_loss(_convert_to_dense(inputs), ragged_output),
            lambda: _call_loss(inputs, ragged_output)))

    exit(loss_fn(*inputs))

if not isinstance(y_true, ragged_tensor.RaggedTensor):
    exit(loss_fn(y_true, y_pred.to_tensor()))

lshape = y_pred.shape.as_list()[1:-1]
if len(lshape) > 0:
    spec = ragged_tensor.RaggedTensorSpec(shape=lshape, dtype=y_pred.dtype)
else:
    spec = tensor_spec.TensorSpec(shape=[], dtype=y_pred.dtype)

nested_splits_list = [rt.nested_row_splits for rt in (y_true, y_pred)]
if y_pred_extra_dim:
    # The last dimension of a categorical prediction may be ragged or not.
    rdims = [len(slist) for slist in nested_splits_list]
    if rdims[0] == rdims[1] - 1:
        nested_splits_list[1] = nested_splits_list[1][:-1]

map_fn = functools.partial(_wrapper, ragged_output=len(lshape) > 1)

assertion_list = ragged_util.assert_splits_match(nested_splits_list)
with ops.control_dependencies(assertion_list):
    exit(ragged_map_ops.map_fn(map_fn, elems=(y_true, y_pred), dtype=spec))
