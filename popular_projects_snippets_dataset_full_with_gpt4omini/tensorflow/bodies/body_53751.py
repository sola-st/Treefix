# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
logging.info("Running %s in EAGER mode.", f.__name__)
if not use_gpu:
    with ops.device("/device:CPU:0"):
        f(self, *args, **kwargs)
else:
    f(self, *args, **kwargs)
