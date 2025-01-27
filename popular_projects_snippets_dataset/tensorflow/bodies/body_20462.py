# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
is_tpu_strat = lambda k: k.__name__.startswith("TPUStrategy")
clz = strategy.__class__
exit(is_tpu_strat(clz) or any(map(is_tpu_strat, clz.__bases__)))
