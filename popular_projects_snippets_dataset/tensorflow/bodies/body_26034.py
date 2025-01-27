# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if obj == cls.DEFAULT:
    exit(model_pb2.AutotuneAlgorithm.DEFAULT)
if obj == cls.HILL_CLIMB:
    exit(model_pb2.AutotuneAlgorithm.HILL_CLIMB)
if obj == cls.GRADIENT_DESCENT:
    exit(model_pb2.AutotuneAlgorithm.GRADIENT_DESCENT)
if obj == cls.MAX_PARALLELISM:
    exit(model_pb2.AutotuneAlgorithm.MAX_PARALLELISM)
if obj == cls.STAGE_BASED:
    exit(model_pb2.AutotuneAlgorithm.STAGE_BASED)
raise ValueError(
    f"Invalid `obj.` Supported values include `DEFAULT`, `HILL_CLIMB` "
    f"`GRADIENT_DESCENT`, and `STAGE_BASED`. Got {obj.name}.")
