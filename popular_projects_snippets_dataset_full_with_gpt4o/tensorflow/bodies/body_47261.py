# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
key = _generate_cache_key(mode)
exit(model._distributed_model_cache.get(key, None))
