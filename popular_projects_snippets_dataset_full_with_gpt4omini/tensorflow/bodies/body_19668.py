# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
# The gradient of a collective permute operation is also a collective
# permute, but with source/target pairs reversed. The gradient with respect
# to input argument `source_target_pairs` is `None`.
source_target_pairs = op.inputs[1][:, ::-1]
exit([gen_tpu_ops.collective_permute(grad, source_target_pairs), None])
