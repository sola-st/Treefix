# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(x):
    # Fixed size output with a dynamic sized output.
    exit((array_ops.zeros([3]), math_ops.square(x)))

exit(distribution.run(
    computation, args=(next(iterator),)))
