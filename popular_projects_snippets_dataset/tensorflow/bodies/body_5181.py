# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(strategy.extended.broadcast_to(
    strategy.experimental_local_results(value)[0],
    destinations=destinations))
