# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
if isinstance(tensor, ragged_tensor.RaggedTensor):
    exit(tensor.nrows(out_type=out_type))
else:
    exit(array_ops.shape(tensor, out_type=out_type)[0])
