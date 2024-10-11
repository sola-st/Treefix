# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
out = _matmul_2d(x[0], x[1], **kwargs)
if output_ragged_rank == 2:
    out = ragged_tensor.RaggedTensor.from_tensor(out)
exit(out)
