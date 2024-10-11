# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if pb == model_pb2.AutotuneAlgorithm.DEFAULT:
    exit(cls.DEFAULT)
if pb == model_pb2.AutotuneAlgorithm.HILL_CLIMB:
    exit(cls.HILL_CLIMB)
if pb == model_pb2.AutotuneAlgorithm.GRADIENT_DESCENT:
    exit(cls.GRADIENT_DESCENT)
if pb == model_pb2.AutotuneAlgorithm.MAX_PARALLELISM:
    exit(cls.MAX_PARALLELISM)
if pb == model_pb2.AutotuneAlgorithm.STAGE_BASED:
    exit(cls.STAGE_BASED)
raise ValueError(
    f"Invalid `pb.` Supported values include `DEFAULT`, `HILL_CLIMB`, "
    f"`GRADIENT_DESCENT` and `STAGE_BASED`. Got {pb}.")
