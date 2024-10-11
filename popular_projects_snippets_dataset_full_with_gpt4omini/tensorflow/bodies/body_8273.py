# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
exit(combinations.combine(
    distribution=[
        strategy_combinations.tpu_strategy_one_step,
        strategy_combinations.tpu_strategy
    ],
    mode=["graph"]))
