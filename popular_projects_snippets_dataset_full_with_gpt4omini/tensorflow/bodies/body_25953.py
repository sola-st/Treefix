# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/sample_from_datasets_op.py
exit(array_ops.squeeze(
    gen_stateless_random_ops.stateless_multinomial(
        logits, 1, seed=seed),
    axis=[0, 1]))
