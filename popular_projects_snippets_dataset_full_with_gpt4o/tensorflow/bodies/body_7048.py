# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
exit((all_strategy_minus_default_and_tpu_combinations() +
        tpu_strategy_combinations()))
