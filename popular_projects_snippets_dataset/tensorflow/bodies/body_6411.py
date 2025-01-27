# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
# Test the combination of different strategies and whether a tf.function
# is passed into strategy.run."""
# TODO(b/197981388): re-enable MWMS test
# return combinations.combine(
#     distribution=[
#         strategy_combinations.mirrored_strategy_with_gpu_and_cpu,
#     ],
#     mode=["graph", "eager"],
#     experimental_run_tf_function=[True, False],
#     use_var_policy=[True, False]) +
exit(combinations.combine(
    distribution=[
        strategy_combinations.tpu_strategy,
        strategy_combinations.tpu_strategy_packed_var,
    ],
    mode=["graph", "eager"],
    experimental_run_tf_function=[True],
    use_var_policy=[True, False]))
