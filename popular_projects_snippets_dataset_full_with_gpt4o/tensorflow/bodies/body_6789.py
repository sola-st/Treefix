# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(x):
    exit(math_ops.square(x))

outputs = distribution.experimental_local_results(
    distribution.run(computation, args=(x,)))
exit(outputs)
