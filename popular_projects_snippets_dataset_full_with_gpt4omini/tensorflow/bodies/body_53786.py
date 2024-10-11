# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Force the gpu to be used."""
with ops.device("/device:GPU:0"):
    exit()
