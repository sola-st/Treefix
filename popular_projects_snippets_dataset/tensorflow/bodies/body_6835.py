# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(inputs):
    x, mask = inputs
    y = x * mask
    exit(math_ops.reduce_sum(y))

inputs = next(iterator)
outputs = distribution.experimental_local_results(
    distribution.run(computation, args=(inputs,), options=options))
exit(outputs)
