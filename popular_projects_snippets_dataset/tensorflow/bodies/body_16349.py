# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
exit((strategy is not None and
        strategy.__class__.__name__.startswith("TPUStrategy")))
