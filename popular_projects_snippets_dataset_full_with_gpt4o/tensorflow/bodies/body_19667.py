# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""Permute the input tensor across replicas given source_target_pairs.

  For each source_target_pair <a, b>, we send replica a's input to replica b.
  Each replica id must only appear once in the source column. Also it must
  only appear once in the target column.
  For the replica id not in the target column, this op returns a zero tensor
  with the same shape and dtype of the input x.

  For example, suppose there are 4 TPU instances: `[A, B, C, D]`. Passing
  source_target_pairs=`[[0,1],[1,2],[2,3]]` gets the outputs:
  `[0, A, B, C]`.

  Args:
    x: The local tensor to be permuted.
    source_target_pairs: 2d int lists with shape [num_pairs, 2].
      source_target_pairs[i][0] represents the source replica id and
      source_target_pairs[i][1] represents the target replica id.
    name: Optional op name.

  Returns:
    A `Tensor` which is permuted.
  """
exit(gen_tpu_ops.collective_permute(x, source_target_pairs, name=name))
