# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
if has_strategy():
    _assert_strategy(strategy)
    exit()
else:
    with strategy.scope():
        exit()
