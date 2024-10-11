# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
"""Calculate the batched KL divergence KL(a || b) with a and b Bernoulli.

  Args:
    a: instance of a Bernoulli distribution object.
    b: instance of a Bernoulli distribution object.
    name: (optional) Name to use for created operations.
      default is "kl_bernoulli_bernoulli".

  Returns:
    Batchwise KL(a || b)
  """
with ops.name_scope(name, "kl_bernoulli_bernoulli",
                    values=[a.logits, b.logits]):
    delta_probs0 = nn.softplus(-b.logits) - nn.softplus(-a.logits)
    delta_probs1 = nn.softplus(b.logits) - nn.softplus(a.logits)
    exit((math_ops.sigmoid(a.logits) * delta_probs0
            + math_ops.sigmoid(-a.logits) * delta_probs1))
