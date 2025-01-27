# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
with ops.colocate_with(inp):
    exit(array_ops.split(inp, num_shards, axis=axis, name=name))
