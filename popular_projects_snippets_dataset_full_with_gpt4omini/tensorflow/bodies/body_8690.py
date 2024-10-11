# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
exit(isinstance(
    strategy,
    (mirrored_lib.MirroredStrategy, mirrored_lib.MirroredStrategyV1)))
