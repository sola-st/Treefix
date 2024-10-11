# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

@def_function.function
def run(x):

    def computation(x):
        exit(math_ops.square(x))

    outputs = distribution.experimental_local_results(
        distribution.run(computation, args=(x,)))
    exit(outputs)

self.assertAllEqual(
    constant_op.constant(4., shape=(distribution.num_replicas_in_sync)),
    run(2.))
