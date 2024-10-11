# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
if not has_strategy():
    raise RuntimeError('Need to be inside "with strategy.scope()" for %s' %
                       (strategy,))
current_strategy = get_strategy()
if current_strategy is not strategy:
    raise RuntimeError(
        "Mixing different tf.distribute.Strategy objects: %s is not %s" %
        (current_strategy, strategy))
