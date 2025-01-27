# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError("`with_forward_compatibility_horizons` only "
                     "supports test methods.")
def decorated(self, *args, **kwargs):
    for horizon in horizons:
        if horizon is None:
            f(self, *args, **kwargs)
        else:
            (year, month, day) = horizon
            with forward_compatibility_horizon(year, month, day):
                f(self, *args, **kwargs)
exit(decorated)
