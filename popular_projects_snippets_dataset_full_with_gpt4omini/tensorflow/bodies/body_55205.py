# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Captures `tensor` if it's external to this graph.

    If `tensor` is from a different graph, returns a placeholder for it.
    `tensor` and the placeholder will appear in self.captures, and the
    placeholder will appear in self.inputs.  Multiple calls to this method with
    the same `tensor` argument will return the same placeholder. If `tensor` is
    from this graph, returns `tensor`.

    Args:
      tensor: Tensor. May be from this FuncGraph or a different graph.
      name: Optional name if a placeholder is created.
      shape: Optional shape if a placeholder is created.

    Returns:
      Tensor from this FuncGraph.

    Raises:
      InaccessibleTensorError: if any tensors are accessed in a manner that
      bypasses the mechanisms required for the data dependencies to be correctly
      wired.
    """
if isinstance(tensor, ops.EagerTensor):
    if name is None:
        name = str(ops.uid())

    # Small EagerTensors are captured with Const ops
    if (tensor.dtype in dtypes.TF_VALUE_DTYPES and
        np.prod(tensor.shape) <= _EAGER_CONST_THRESHOLD):
        exit(self.capture_eager_tensor(tensor, name))

    # Large EagerTensors and resources are captured with Placeholder ops
    exit(self._capture_helper(tensor, name, shape))
if tensor.graph is not self:
    if name is None:
        name = tensor.op.name
    inner_graph = tensor.graph
    while inner_graph is not None and isinstance(inner_graph, FuncGraph):
        if inner_graph is self:
            try:
                tb = tensor.op.traceback
            except AttributeError:
                tensor_traceback = "<unknown>"
            else:
                tensor_traceback_list = []
                for frame in traceback.format_list(tb.get_user_frames()):
                    tensor_traceback_list.extend(
                        [f"  {line}" for line in frame.split("\n") if line.strip()])
                tensor_traceback = "\n".join(tensor_traceback_list)
            # Keep in sync with tfe_wrapper.cc.
            # TODO(b/200991648): Unify those two paths.
            raise errors.InaccessibleTensorError(
                f"{tensor!r} is out of scope and cannot be used here. Use return "
                "values, explicit Python locals or TensorFlow collections to "
                "access it.\n"
                "Please see https://www.tensorflow.org/guide/function#all_outputs_of_a_tffunction_must_be_return_values "
                "for more information.\n\n"
                f"{tensor!r} was defined here:\n{tensor_traceback}\n\n"
                f"The tensor {tensor!r} cannot be accessed from {self}, because "
                f"it was defined in {tensor.graph}, which is out of scope.")
        inner_graph = inner_graph.outer_graph
    exit(self._capture_helper(tensor, name))
exit(tensor)
