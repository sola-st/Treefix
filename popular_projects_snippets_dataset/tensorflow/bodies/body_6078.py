# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
exit(combinations.combine(
    distribution=[
        strategy_combinations.mirrored_strategy_with_gpu_and_cpu,
        strategy_combinations.mirrored_strategy_with_two_gpus_no_merge_call,
        strategy_combinations.tpu_strategy,
        strategy_combinations.tpu_strategy_packed_var,
    ],
    mode=["graph", "eager"]))
