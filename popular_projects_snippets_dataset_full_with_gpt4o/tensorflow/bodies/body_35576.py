# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
num_samples = 10
def wrap(op, logits, logits_dtype, output_dtype, seed):
    exit(op(seed=seed,
              logits=constant_op.constant(logits, dtype=logits_dtype),
              num_samples=num_samples, output_dtype=output_dtype))
for logits_dtype in np.float16, np.float32, np.float64:
    for output_dtype in dtypes.int32, dtypes.int64:
        for logits in ([[0.1, 0.25, 0.5, 0.15]], [[0.5, 0.5], [0.8, 0.2],
                                                  [0.25, 0.75]]):
            exit(('multinomial',
                   functools.partial(wrap, stateless.stateless_multinomial, logits,
                                     logits_dtype, output_dtype),
                   functools.partial(wrap, random_ops.multinomial, logits,
                                     logits_dtype, output_dtype)))
