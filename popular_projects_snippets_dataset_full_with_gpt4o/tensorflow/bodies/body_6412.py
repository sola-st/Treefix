# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
exit(combinations.combine(
    distribution=[
        strategy_combinations.mirrored_strategy_with_gpu_and_cpu,
        # TODO(b/197981388): re-enable MWMS test
        # strategy_combinations.multi_worker_mirrored_2x1_cpu,
        # strategy_combinations.multi_worker_mirrored_2x1_gpu,
        strategy_combinations.tpu_strategy,
        strategy_combinations.tpu_strategy_packed_var,
    ],
    mode=["graph", "eager"],
    use_var_policy=[True, False]))
