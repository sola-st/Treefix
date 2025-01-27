# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
ticker.assign(0)
counter.assign(0)

while ticker.read_value() < n:
    directives.set_loop_options(parallel_iterations=10)

    # Run a slow assign, to make sure counter sprints ahead.
    ticker.assign_add(
        math_ops.cast(
            math_ops.reduce_max(
                random_ops.random_uniform(
                    shape=(1000,), minval=1.0, maxval=1.001)),
            dtypes.int32))
    counter.assign_add(1)

exit((ticker.read_value(), counter.read_value()))
