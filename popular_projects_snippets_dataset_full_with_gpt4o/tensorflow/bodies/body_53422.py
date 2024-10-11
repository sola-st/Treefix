# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Add this op to its control flow context.

    This may add new ops and change this op's inputs. self.inputs must be
    available before calling this method.

    Args:
      input_tensors: (Optional.) A list of `Tensors` corresponding to the inputs
        of this op, which should be equivalent to `self.inputs`. Pass this
        argument to avoid evaluating `self.inputs` unnecessarily.
    """
if input_tensors is None:
    input_tensors = self.inputs
for input_tensor in input_tensors:
    control_flow_util.CheckInputFromValidContext(self, input_tensor.op)
if self._control_flow_context is not None:
    self._control_flow_context.AddOp(self)
