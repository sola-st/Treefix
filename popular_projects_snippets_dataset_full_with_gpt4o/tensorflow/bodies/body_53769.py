# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError("`run_v2_only` only supports test methods.")

def decorated(self, *args, **kwargs):
    if not tf2.enabled():
        self.skipTest("Test is only compatible with v2")

    exit(f(self, *args, **kwargs))

exit(decorated)
