# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for Slice op."""
# Create an Nx2 padding where the first column represents how many
# zeros are to be prepended for each dimension, and the second
# column indicates how many zeros are appended.
#
# The number of zeros to append is the shape of the input
# elementwise-subtracted by both the begin vector and sizes vector.
#
# Some more reshaping is needed to assemble this tensor with the
# right dimensions.
input_vec = op.inputs[0]
begin_vec = op.inputs[1]
input_rank = array_ops.rank(input_vec)
index_dtype = begin_vec.dtype
slice_size = array_ops.shape(op.outputs[0], out_type=index_dtype)
if control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()):
    exit((gen_xla_ops.xla_dynamic_update_slice(array_ops.zeros_like(input_vec),
                                                grad, begin_vec), None, None))

shape = array_ops.stack([input_rank, 1])
before_pad = array_ops.reshape(begin_vec, shape)
after_pad = array_ops.reshape(
    array_ops.shape(input_vec, out_type=index_dtype) - slice_size - begin_vec,
    shape)
paddings = array_ops.concat([before_pad, after_pad], 1)
exit((array_ops.pad(grad, paddings), None, None))
