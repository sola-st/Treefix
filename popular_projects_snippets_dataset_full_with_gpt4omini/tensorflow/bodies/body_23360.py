# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
supported_strategies = [s.lower() for s in supported_profile_strategies()]
if strategy.lower() not in supported_strategies:
    raise ValueError(
        ("profile_strategy '{}' is not supported. It should be one of {}"
        ).format(strategy, supported_profile_strategies()))
if strategy == "ImplicitBatchModeCompatible":
    logging.warn(
        "ImplicitBatchModeCompatible strategy is deprecated, and"
        " using it may result in errors during engine building. Please"
        " consider using a different profile strategy.")
