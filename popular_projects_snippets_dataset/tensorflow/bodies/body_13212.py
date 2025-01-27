# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
with func_graph.as_default():
    exit([gen_optional_ops.optional_from_value([t]) for t in intermediates])
