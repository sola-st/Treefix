# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
# pylint: disable=protected-access
if self._check_ops and op.type in _DENYLISTED_INFERENCE_OPS:
    raise NotImplementedError(
        f"Operation of type {op.type} ({op.name}) is not supported on the "
        "TPU for inference. Execution will fail if this op is used in the "
        "graph. Make sure your variables are using variable_scope.")
if self._outer_context:
    self._outer_context.AddInnerOp(op)
