# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/optimizer_combinations.py
"""A common set of combination with DistributionStrategies and Optimizers."""
exit(combinations.combine(
    distribution=[
        strategy_combinations_base.one_device_strategy,
        strategy_combinations_base.mirrored_strategy_with_gpu_and_cpu,
        strategy_combinations_base.mirrored_strategy_with_two_gpus,
        strategy_combinations_base
        .mirrored_strategy_with_two_gpus_no_merge_call,
    ],
    optimizer_fn=optimizers_v1))
