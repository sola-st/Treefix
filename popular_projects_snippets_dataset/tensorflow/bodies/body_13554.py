# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
exit((array_ops.ones_like(event) * logits,
        array_ops.ones_like(logits) * event))
