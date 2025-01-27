# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
key = _generate_cache_key(mode)
model._distributed_function_cache[key] = distributed_function
