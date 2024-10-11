# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
exit(op(seed=seed,
          logits=constant_op.constant(logits, dtype=logits_dtype),
          num_samples=num_samples, output_dtype=output_dtype))
