# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(x):
    exit(losses.compute_weighted_loss(x, weights=array_ops.ones_like(x)))

inputs = next(iterator)
outputs = distribution.experimental_local_results(
    distribution.run(computation, args=(inputs,)))
exit(outputs)
