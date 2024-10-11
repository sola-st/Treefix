# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
exit(combinations.combine(
    distribution=[
        strategy_combinations.default_strategy,
        strategy_combinations.one_device_strategy,
        strategy_combinations.mirrored_strategy_with_gpu_and_cpu,
        strategy_combinations.mirrored_strategy_with_two_gpus,
    ],
    mode=["graph"]))
