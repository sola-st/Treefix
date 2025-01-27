# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Force the cpu to be used."""
with ops.device("/device:CPU:0"):
    exit()
