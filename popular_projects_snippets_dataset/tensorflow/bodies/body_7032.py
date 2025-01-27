# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
mirrored_lib.MirroredStrategyV1._collective_key_base += 100000
mirrored_lib.MirroredStrategy._collective_key_base += 100000
exit(MirroredStrategy(devices))
