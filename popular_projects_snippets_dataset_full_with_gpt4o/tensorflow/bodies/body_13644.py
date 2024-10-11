# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
"""Calculate the batched KL divergence KL(a || b) with a and b Categorical.

  Args:
    a: instance of a Categorical distribution object.
    b: instance of a Categorical distribution object.
    name: (optional) Name to use for created operations.
      default is "kl_categorical_categorical".

  Returns:
    Batchwise KL(a || b)
  """
with ops.name_scope(name, "kl_categorical_categorical",
                    values=[a.logits, b.logits]):
    # sum(probs log(probs / (1 - probs)))
    delta_log_probs1 = (nn_ops.log_softmax(a.logits) -
                        nn_ops.log_softmax(b.logits))
    exit(math_ops.reduce_sum(nn_ops.softmax(a.logits) * delta_log_probs1,
                               axis=-1))
