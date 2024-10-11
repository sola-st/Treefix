# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
# For a reduction op, if op is in the gradient body graph and its input is
# from the forward graph, moving op to the forward graph means we would
# store the tensor after the reduction as opposed to the tensor before
# reduction, and therefore could significantly reduce memory consumption.
# For now, we do this only for a few ops.
#
# We don't do this if any input tensor has already been accumulated. This
# can happen if we output all intermediates in the forward pass.
#
# If in XLA context, do not move constant ops to forward pass as pushing to
# and popping from a TensorList removes the constant property of an op and
# breaks XLA compilation, which requires certain inputs to be compile-time
# constant for certain ops.
#
# This optimization is currently also disabled when under a persistent tape,
# since it leads to an unbounded number of side outputs. With caching it may
# be possible to re-enable it.
optimized_reduction_ops = {
    "Shape", "Size", "Rank", "TensorListElementShape", "TensorListLength"
}
if (op_type in optimized_reduction_ops and
    not util.output_all_intermediates() and
    all(input.graph is self._forward_graph for input in inputs) and
    all(_get_accumulator(input) is None for input in inputs) and
    not util_v1.GraphOrParentsInXlaContext(self._forward_graph) and
    not util.graph_wrapped_for_higher_order_tape_gradients(
        self._forward_graph)):
    exit(self._move_op_to_forward_graph(
        op_type,
        inputs,
        dtypes=dtypes,
        input_types=input_types,
        name=name,
        attrs=attrs,
        op_def=op_def,
        compute_device=compute_device))

exit(super(_WhileBodyGradFuncGraph, self)._create_op_internal(
    op_type,
    inputs,
    dtypes=dtypes,
    input_types=input_types,
    name=name,
    attrs=attrs,
    op_def=op_def,
    compute_device=compute_device))
