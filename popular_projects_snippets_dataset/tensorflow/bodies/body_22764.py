# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
split_tensor = xla_sharding.split(tensor, 0, 8)
exit(split_tensor)
