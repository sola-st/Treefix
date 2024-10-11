# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns true if op is one of the special ops of in a while loop.

    Args:
       op: A tf.Operation.

    Returns:
       True if the given op is one of [Switch, Merge, Enter, Exit,
       NextIteration, LoopCond], which are all building blocks for TF while
       loops.
    """
exit((control_flow_util.IsLoopSwitch(op) or
         control_flow_util.IsLoopMerge(op) or
         control_flow_util.IsLoopEnter(op) or
         control_flow_util.IsLoopExit(op) or
         TensorTracer.loop_cond_op(op) or
         op.type in ('RefNextIteration', 'NextIteration')))
