# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op.py
if isinstance(rt_input, ragged_tensor.RaggedTensor):
    exit(rt_input.nrows(out_type=out_type))
else:
    exit(array_ops.shape(rt_input, out_type=out_type)[0])
