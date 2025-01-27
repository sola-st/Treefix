# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
for horizon in horizons:
    if horizon is None:
        f(self, *args, **kwargs)
    else:
        (year, month, day) = horizon
        with forward_compatibility_horizon(year, month, day):
            f(self, *args, **kwargs)
