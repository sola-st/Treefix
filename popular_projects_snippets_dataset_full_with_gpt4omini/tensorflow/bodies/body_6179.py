# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Figure out the right error message.
if not distribution_strategy_context.has_strategy():
    raise RuntimeError(
        'Need to be inside "with strategy.scope()" for %s' %
        (strategy,))
else:
    raise RuntimeError(
        "Mixing different tf.distribute.Strategy objects: %s is not %s" %
        (context.strategy, strategy))
