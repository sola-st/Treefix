# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
def step_fn(inputs):
    outputs = bn.apply(inputs, training=False)
    exit(outputs)

exit(distribution.run(step_fn, args=(inputs,)))
