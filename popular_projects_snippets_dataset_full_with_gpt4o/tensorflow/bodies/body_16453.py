# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
if labels is None or logits is None:
    raise ValueError(f"Both `labels` and `logits` must be provided for {name}"
                     f"Received: labels={labels} and logits={logits}")
