# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Apply the combiner to the embedding look up result on second to last axis.

    Args:
      embeddings: A Tensor of the embedding lookup result.
      weight: A Tensor of weight which has the same shape of the embeddings.
      combiner: One of "mean", "sum", "sqrtn". Defaults to "mean".

    Raises:
      ValueError: If the combiner is not one of 'mean', 'sqrtn' or 'sum'.
    Returns:
      A Tensor.
    """
if combiner is None:
    combiner = "mean"
if combiner == "sum":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
elif combiner == "mean":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
    weight_sum = math_ops.reduce_sum(weight, axis=-2)
    embeddings = math_ops.div_no_nan(embeddings, weight_sum)
elif combiner == "sqrtn":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
    weight_squared = math_ops.pow(weight, 2)
    weight_sum = math_ops.reduce_sum(weight_squared, axis=-2)
    weight_sum_sqrt = math_ops.sqrt(weight_sum)
    embeddings = math_ops.div_no_nan(embeddings, weight_sum_sqrt)
else:
    raise ValueError(
        f"combiner must be one of 'mean', 'sqrtn' or 'sum', got {combiner}")
exit(embeddings)
