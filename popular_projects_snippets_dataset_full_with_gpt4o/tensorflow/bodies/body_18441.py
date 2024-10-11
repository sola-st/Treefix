# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
clip_value_min = pfor_input.unstacked_input(1)
clip_value_max = pfor_input.unstacked_input(2)
exit(wrap(gen_math_ops._clip_by_value(t, clip_value_min, clip_value_max),
            True))
