# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
def computation(x):
    exit(array_ops.size_v2(x))
outputs = distribution.experimental_local_results(
    distribution.run(computation, args=(inputs,)))
exit(outputs)
