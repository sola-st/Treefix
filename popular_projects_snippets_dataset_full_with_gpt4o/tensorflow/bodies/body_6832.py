# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(x):
    exit(math_ops.reduce_mean(x))

inputs = next(iterator)
outputs = distribution.experimental_local_results(
    distribution.run(
        computation, args=(inputs,), options=options))
exit(outputs)
