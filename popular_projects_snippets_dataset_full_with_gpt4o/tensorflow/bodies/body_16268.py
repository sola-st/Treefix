# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if isinstance(tensor, RaggedTensor):
    exit(tensor.nrows(out_type=out_type))
else:
    exit(array_ops.shape(tensor, out_type=out_type)[0])
