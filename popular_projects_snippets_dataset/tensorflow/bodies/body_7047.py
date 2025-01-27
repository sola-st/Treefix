# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
exit(combinations.combine(
    distribution=[
        one_device_strategy, one_device_strategy_gpu,
        mirrored_strategy_with_gpu_and_cpu, mirrored_strategy_with_two_gpus
    ],
    mode=["graph", "eager"]))
