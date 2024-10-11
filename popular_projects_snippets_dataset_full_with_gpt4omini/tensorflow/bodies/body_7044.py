# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
exit(combinations.combine(
    distribution=strategies_minus_tpu, mode=["graph", "eager"]))
