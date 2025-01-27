# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
exit(combinations.combine(
    distribution=[
        strategy_combinations.mirrored_strategy_with_one_cpu,
        strategy_combinations.mirrored_strategy_with_one_gpu,
    ],
    mode=["graph", "eager"]))
